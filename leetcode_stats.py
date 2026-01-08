import requests

url = "https://leetcode.com/graphql"
query = """
query getUserProfile($username: String!) {
  matchedUser(username: $username) {
    username
    profile {
      ranking
      userAvatar
      realName
    }
    submitStats {
      acSubmissionNum {
        difficulty
        count
      }
    }
  }
}
"""

response = requests.post(url, json={"query": query, "variables": {"username": "vijaya262001"}})
data = response.json()

if 'data' in data and data['data']['matchedUser']:
    profile = data['data']['matchedUser']
    print("Username:", profile['username'])
    print("Real Name:", profile['profile']['realName'])
    print("Ranking:", profile['profile']['ranking'])
    print("Solved Problems:")
    for item in profile['submitStats']['acSubmissionNum']:
        print(f"  {item['difficulty']}: {item['count']}")
else:
    print("Failed to fetch data")
    print("Response:", data)