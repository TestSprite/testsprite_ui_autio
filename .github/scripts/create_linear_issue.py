# -*- coding: utf-8 -*- 
# 姓名：李万伦
# 时间：2025/11/21  23:33
# 文件名：create_linear_issue.py.py
"""
自动创建Linear Issue的脚本
针对测试失败的场景
"""

import os
import json
import glob
import requests
from datetime import datetime
import re


def parse_test_results():
    """解析测试结果，提取失败用例信息"""
    failed_tests = []

    print("开始解析测试结果...")

    # 解析Allure结果文件
    for result_file in glob.glob("results/*.json"):
        try:
            with open(result_file, 'r', encoding='utf-8') as f:
                test_data = json.load(f)

            # 检查测试状态
            status = test_data.get('status', '')
            if status in ['failed', 'broken']:
                test_name = test_data.get('name', 'Unknown Test')
                full_name = test_data.get('fullName', '')

                # 提取错误信息
                error_info = extract_error_info(test_data)

                # 分类测试类型
                test_category = categorize_test(full_name)

                failed_tests.append({
                    'name': test_name,
                    'full_name': full_name,
                    'category': test_category,
                    'status': status,
                    'error_message': error_info.get('message', ''),
                    'error_trace': error_info.get('trace', ''),
                    'timestamp': test_data.get('start', datetime.now().timestamp())
                })

        except Exception as e:
            print(f"解析文件 {result_file} 时出错: {e}")
            continue

    return failed_tests


def extract_error_info(test_data):
    """从测试数据中提取错误信息"""
    error_info = {'message': '', 'trace': ''}

    status_details = test_data.get('statusDetails', {})
    if status_details:
        error_info['message'] = status_details.get('message', '')[:500]
        error_info['trace'] = status_details.get('trace', '')[:1000]

    return error_info


def categorize_test(test_full_name):
    """根据测试名称分类"""
    test_full_name = test_full_name.upper()

    if 'test_Dashboard_OVERVIEW' in test_full_name:
        return 'OVERVIEW'
    elif 'test_Dashboard_PersonalCenter' in test_full_name:
        return 'PersonalCenter'
    elif 'test_Dashboard_SETTINGS' in test_full_name:
        return 'SETTINGS'
    elif 'test_Dashboard_TESTING' in test_full_name:
        return 'TESTING'
    elif 'test_HomePage' in test_full_name:
        return 'HomePage'
    elif 'test_User_Login' in test_full_name:
        return 'Login'
    elif 'test_User_Registration' in test_full_name:
        return 'Registration'
    else:
        return 'others'


def create_linear_issue(failed_tests):
    """创建Linear Issue"""

    # 获取环境变量
    api_key = os.getenv('LINEAR_API_KEY')
    team_id = os.getenv('LINEAR_TEAM_ID')
    repo = os.getenv('GITHUB_REPOSITORY', 'unknown/repo')
    sha = os.getenv('GITHUB_SHA', '')[:8]
    run_id = os.getenv('GITHUB_RUN_ID', 'unknown')
    actor = os.getenv('GITHUB_ACTOR', 'unknown')

    if not api_key:
        print("❌ 错误: LINEAR_API_KEY 未设置")
        return False

    if not team_id:
        print("❌ 错误: LINEAR_TEAM_ID 未设置")
        return False

    # 构建Issue标题
    current_time = datetime.now().strftime("%m/%d %H:%M")
    title = f"UI测试失败: {len(failed_tests)}个用例失败 - {sha}"

    # 构建详细的Issue描述
    description = f"""## 🚨 UI自动化测试失败报告

### 📊 执行概览
- **仓库**: `{repo}`
- **Commit**: `{sha}`
- **触发者**: {actor}
- **执行时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- **失败用例数**: {len(failed_tests)}

### ❌ 失败用例详情
"""

    # 按类别分组显示失败用例
    categories = {}
    for test in failed_tests:
        category = test['category']
        if category not in categories:
            categories[category] = []
        categories[category].append(test)

    for category, tests in categories.items():
        description += f"\n#### 📁 {category} ({len(tests)}个失败)\n"

        for i, test in enumerate(tests, 1):
            description += f"""
**{i}. {test['name']}**
- **状态**: `{test['status']}`
- **完整路径**: `{test['full_name']}`

**错误信息**:"""
            if test['error_trace']:
                description += f"**堆栈跟踪**:\n```\n{test['error_trace'][:800]}...\n```\n"

    description += f"""
### 🔍 问题分析

根据失败模式，可能的问题包括：
- 页面元素定位失败
- 网络请求超时
- 数据验证不通过
- 功能逻辑变更

### 🔗 相关链接
- [📋 GitHub Actions运行详情](https://github.com/{repo}/actions/runs/{run_id})
- [📊 测试报告](https://github.com/{repo}/actions/runs/{run_id})
- [🔍 代码变更](https://github.com/{repo}/commit/{os.getenv('GITHUB_SHA')})

### ✅ 处理建议
1. 查看详细的测试报告确认失败原因
2. 检查相关功能页面是否正常
3. 验证测试数据和环境配置
4. 修复问题后重新运行测试验证

---

*自动创建于 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
"""

    # Linear GraphQL API配置
    graphql_url = "https://api.linear.app/graphql"

    mutation = """
    mutation CreateIssue($input: IssueCreateInput!) {
      issueCreate(input: $input) {
        success
        issue {
          id
          title
          identifier
          url
          state {
            name
          }
        }
      }
    }
    """

    variables = {
        "input": {
            "teamId": team_id,
            "title": title,
            "description": description,
            "priority": 2,  # 高优先级
            "labelIds": ["UI-Test-Failure"]  # 可选的标签
        }
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": api_key
    }

    try:
        print("📡 正在向Linear发送请求...")
        response = requests.post(
            graphql_url,
            json={"query": mutation, "variables": variables},
            headers=headers,
            timeout=30
        )

        if response.status_code == 200:
            result = response.json()

            if "errors" in result:
                print(f"❌ Linear API返回错误: {result['errors']}")
                return False

            issue_data = result.get("data", {}).get("issueCreate", {})
            if issue_data.get("success"):
                issue = issue_data["issue"]
                print(f"✅ Linear Issue创建成功!")
                print(f"   📝 Issue编号: {issue['identifier']}")
                print(f"   🔗 访问链接: {issue['url']}")
                print(f"   📄 标题: {issue['title']}")
                print(f"   📊 状态: {issue['state']['name']}")
                return True
            else:
                print("❌ 创建Linear Issue失败")
                return False
        else:
            print(f"❌ HTTP请求失败: {response.status_code}")
            print(f"   响应内容: {response.text}")
            return False

    except Exception as e:
        print(f"❌ 创建Linear Issue时发生异常: {e}")
        return False

def main():
    """主函数"""
    print("=" * 60)
    print("🚀 开始处理测试失败结果")
    print("=" * 60)

    # 解析失败测试
    failed_tests = parse_test_results()

    if not failed_tests:
        print("✅ 没有发现失败测试，无需创建Issue")
        return

    print(f"📊 发现 {len(failed_tests)} 个失败测试用例:")
    for test in failed_tests:
        print(f"   • {test['category']} - {test['name']}")

    print("\n📨 开始创建Linear Issue...")
    success = create_linear_issue(failed_tests)

    if success:
        print("🎉 Linear Issue创建成功!")
    else:
        print("💥 Linear Issue创建失败")

    print("=" * 60)

if __name__ == "__main__":
    main()