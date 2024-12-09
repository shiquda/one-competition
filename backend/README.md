# 后端API文档

本文档详细介绍了后端所有可用的API接口，包括请求方法、URL、描述、请求参数、请求示例、响应示例以及权限要求。

## 目录

1. [用户认证相关](#用户认证相关)
    - [用户注册](#用户注册)
    - [用户登录](#用户登录)
    - [修改密码](#修改密码)
    - [Token刷新](#token刷新)
2. [竞赛相关](#竞赛相关)
    - [获取所有已审核的竞赛](#获取所有已审核的竞赛)
    - [获取竞赛详情](#获取竞赛详情)
    - [添加竞赛](#添加竞赛)
    - [删除竞赛](#删除竞赛)
    - [获取所有竞赛（管理员）](#获取所有竞赛管理员)
    - [更新竞赛](#更新竞赛)
    - [投稿竞赛](#投稿竞赛)

---

## 用户认证相关

### 用户注册

- **URL:** `/api/auth/register/`
- **请求方法:** `POST`
- **描述:** 允许新用户注册账户。
- **权限:** 允许任何人访问 (`AllowAny`)

#### 请求参数

| 参数           | 类型   | 必填 | 描述           |
| -------------- | ------ | ---- | -------------- |
| `username`     | string | 是   | 用户名，需唯一 |
| `password`     | string | 是   | 密码           |
| `email`        | string | 否   | 用户邮箱，需唯一 |

#### 请求示例

```json
{
  "username": "john_doe",
  "password": "SecurePass123",
  "email": "john@example.com"
}
```

#### 响应示例

- **成功（201 Created）**

```json
{
  "message": "注册成功",
  "token": "jwt_access_token",
  "refresh": "jwt_refresh_token",
  "username": "john_doe",
  "user_type": "regular"
}
```

- **失败（400 Bad Request）**

```json
{
  "error": "用户名已存在"
}
```

### 用户登录

- **URL:** `/api/auth/login/`
- **请求方法:** `POST`
- **描述:** 允许已注册用户登录。
- **权限:** 允许任何人访问 (`AllowAny`)

#### 请求参数

| 参数       | 类型   | 必填 | 描述           |
| ---------- | ------ | ---- | -------------- |
| `username` | string | 是   | 用户名或邮箱   |
| `password` | string | 是   | 密码           |

#### 请求示例

```json
{
  "username": "john_doe",
  "password": "SecurePass123"
}
```

#### 响应示例

- **成功（200 OK）**

```json
{
  "message": "登录成功",
  "token": "jwt_access_token",
  "refresh": "jwt_refresh_token",
  "username": "john_doe",
  "user_type": "regular"
}
```

- **失败（401 Unauthorized）**

```json
{
  "error": "用户名或密码错误"
}
```

### 修改密码

- **URL:** `/api/auth/change_password/`
- **请求方法:** `POST`
- **描述:** 允许已认证用户修改密码。
- **权限:** 需要用户认证 (`IsAuthenticated`)

#### 请求参数

| 参数               | 类型   | 必填 | 描述       |
| ------------------ | ------ | ---- | ---------- |
| `old_password`     | string | 是   | 旧密码     |
| `new_password`     | string | 是   | 新密码     |
| `confirm_password` | string | 是   | 确认新密码 |

#### 请求示例

```json
{
  "old_password": "OldPass123",
  "new_password": "NewSecurePass456",
  "confirm_password": "NewSecurePass456"
}
```

#### 响应示例

- **成功（200 OK）**

```json
{
  "message": "密码修改成功"
}
```

- **失败（400 Bad Request）**

```json
{
  "error": "旧密码不正确"
}
```

### Token刷新

- **URL:** `/api/auth/refresh/`
- **请求方法:** `POST`
- **描述:** 使用刷新令牌获取新的访问令牌。
- **权限:** 需要刷新令牌

#### 请求参数

| 参数      | 类型   | 必填 | 描述           |
| --------- | ------ | ---- | -------------- |
| `refresh` | string | 是   | 刷新令牌       |

#### 请求示例

```json
{
  "refresh": "jwt_refresh_token"
}
```

#### 响应示例

- **成功（200 OK）**

```json
{
  "access": "new_jwt_access_token"
}
```

- **失败（401 Unauthorized）**

```json
{
  "detail": "Token is invalid or expired"
}
```

---

## 竞赛相关

### 获取所有已审核的竞赛

- **URL:** `/api/competitions/`
- **请求方法:** `GET`
- **描述:** 获取所有审核通过的竞赛信息。
- **权限:** 允许任何人访问

#### 请求示例

无需请求体。

#### 响应示例

- **成功（200 OK）**

```json
[
  {
    "id": 1,
    "name": "全国大学生数学竞赛",
    "types": ["数学", "学术"],
    "levels": ["全国级"],
    "description": "这是一个面向全国大学生的数学竞赛。",
    "website": "https://math_competition.example.com",
    "other_info": "更多信息请访问官网。",
    "review_status": "approved",
    "timeline": [
      {
        "node_name": "start_time",
        "date": "2024-05-01"
      },
      {
        "node_name": "end_time",
        "date": "2024-05-15"
      }
    ]
  },
  {
    "id": 2,
    "name": "省级编程大赛",
    "types": ["编程", "技术"],
    "levels": ["省级"],
    "description": "这是一个面向省级学生的编程竞赛。",
    "website": "https://provincial_prog_competition.example.com",
    "other_info": "",
    "review_status": "approved",
    "timeline": [
      {
        "node_name": "start_time",
        "date": "2024-06-01"
      },
      {
        "node_name": "end_time",
        "date": "2024-06-10"
      }
    ]
  }
]
```

### 获取竞赛详情

- **URL:** `/api/competition/<int:competition_id>/`
- **请求方法:** `GET`
- **描述:** 获取指定ID的竞赛详细信息，仅限审核通过的竞赛。
- **权限:** 允许任何人访问

#### 请求参数

| 参数           | 类型    | 必填 | 描述          |
| -------------- | ------- | ---- | ------------- |
| `competition_id`| integer | 是   | 竞赛的唯一ID |

#### 请求示例

```http
GET /api/competition/1/
```

#### 响应示例

- **成功（200 OK）**

```json
{
  "id": 1,
  "name": "全国大学生数学竞赛",
  "types": ["数学", "学术"],
  "levels": ["全国级"],
  "description": "这是一个面向全国大学生的数学竞赛。",
  "website": "https://math_competition.example.com",
  "other_info": "更多信息请访问官网。",
  "timeline": [
    {
      "node_name": "start_time",
      "date": "2024-05-01"
    },
    {
      "node_name": "end_time",
      "date": "2024-05-15"
    }
  ]
}
```

- **失败（403 Forbidden）**

```json
{
  "error": "该竞赛尚未通过审核或已被拒绝"
}
```

- **失败（404 Not Found）**

```json
{
  "error": "找不到指定的竞赛"
}
```

### 添加竞赛

- **URL:** `/api/competition/add/`
- **请求方法:** `POST`
- **描述:** 由管理员添加新的竞赛信息。
- **权限:** 需要管理员权限 (`admin_required`)

#### 请求参数

| 参数           | 类型    | 必填 | 描述                      |
| -------------- | ------- | ---- | ------------------------- |
| `name`         | string  | 是   | 竞赛名称                  |
| `types`        | array   | 是   | 竞赛类型列表              |
| `levels`       | array   | 是   | 竞赛级别列表              |
| `description`  | string  | 是   | 竞赛描述                  |
| `website`      | string  | 是   | 竞赛官方网站URL           |
| `timeline`     | object  | 是   | 时间节点，包含`start_time`和`end_time` |
| `other_info`   | string  | 否   | 其他信息                  |

#### 请求示例

```json
{
  "name": "全国大学生数学竞赛",
  "types": ["数学", "学术"],
  "levels": ["全国级"],
  "description": "这是一个面向全国大学生的数学竞赛。",
  "website": "https://math_competition.example.com",
  "timeline": {
    "start_time": "2024-05-01",
    "end_time": "2024-05-15"
  },
  "other_info": "更多信息请访问官网。"
}
```

#### 响应示例

- **成功（201 Created）**

```json
{
  "message": "竞赛创建成功",
  "id": 3
}
```

- **失败（400 Bad Request）**

```json
{
  "error": "缺少字段: name, types"
}
```

- **失败（500 Internal Server Error）**

```json
{
  "error": "创建竞赛时发生服务器错误"
}
```

### 删除竞赛

- **URL:** `/api/competition/delete/<int:competition_id>/`
- **请求方法:** `DELETE`
- **描述:** 由管理员删除指定ID的竞赛。
- **权限:** 需要管理员权限 (`admin_required`)

#### 请求参数

| 参数           | 类型    | 必填 | 描述          |
| -------------- | ------- | ---- | ------------- |
| `competition_id`| integer | 是   | 竞赛的唯一ID |

#### 请求示例

```http
DELETE /api/competition/delete/3/
```

#### 响应示例

- **成功（200 OK）**

```json
{
  "message": "竞赛删除成功"
}
```

- **失败（404 Not Found）**

```json
{
  "error": "找不到指定的竞赛"
}
```

- **失败（500 Internal Server Error）**

```json
{
  "error": "删除竞赛时发生服务器错误: 具体错误信息"
}
```

### 获取所有竞赛（管理员）

- **URL:** `/api/admin/competitions/`
- **请求方法:** `GET`
- **描述:** 由管理员获取所有竞赛信息，包括未审核的竞赛。
- **权限:** 需要管理员权限 (`IsAuthenticated` 且 `user_type` 为 `admin`)

#### 请求示例

无需请求体。

#### 响应示例

- **成功（200 OK）**

```json
[
  {
    "id": 1,
    "name": "全国大学生数学竞赛",
    "types": ["数学", "学术"],
    "levels": ["全国级"],
    "description": "这是一个面向全国大学生的数学竞赛。",
    "website": "https://math_competition.example.com",
    "other_info": "更多信息请访问官网。",
    "review_status": "approved",
    "timeline": [
      {
        "node_name": "start_time",
        "date": "2024-05-01"
      },
      {
        "node_name": "end_time",
        "date": "2024-05-15"
      }
    ]
  },
  {
    "id": 3,
    "name": "省级编程大赛",
    "types": ["编程", "技术"],
    "levels": ["省级"],
    "description": "这是一个面向省级学生的编程竞赛。",
    "website": "https://provincial_prog_competition.example.com",
    "other_info": "",
    "review_status": "pending",
    "timeline": [
      {
        "node_name": "start_time",
        "date": "2024-06-01"
      },
      {
        "node_name": "end_time",
        "date": "2024-06-10"
      }
    ]
  }
]
```

- **失败（403 Forbidden）**

```json
{
  "error": "权限不足，仅管理员可访问此接口"
}
```

### 更新竞赛

- **URL:** `/api/competition/update/<int:competition_id>/`
- **请求方法:** `PUT`
- **描述:** 由管理员更新指定ID的竞赛信息的审核状态。
- **权限:** 需要管理员权限

#### 请求参数

| 参数           | 类型   | 必填 | 描述                   |
| -------------- | ------ | ---- | ---------------------- |
| `review_status` | string | 是   | 审核状态，值为`approved`或`rejected` |

#### 请求示例

```json
{
  "review_status": "approved"
}
```

#### 响应示例

- **成功（200 OK）**

```json
{
  "message": "审核状态更新成功"
}
```

- **失败（400 Bad Request）**

```json
{
  "error": "无效的审核状态"
}
```

- **失败（404 Not Found）**

```json
{
  "error": "找不到指定的竞赛"
}
```

### 投稿竞赛

- **URL:** `/api/competition/submit/`
- **请求方法:** `POST`
- **描述:** 允许普通用户提交新的竞赛信息，待管理员审核。
- **权限:** 需要用户认证 (`IsAuthenticated`)

#### 请求参数

| 参数           | 类型    | 必填 | 描述                      |
| -------------- | ------- | ---- | ------------------------- |
| `name`         | string  | 是   | 竞赛名称                  |
| `types`        | array   | 是   | 竞赛类型列表              |
| `levels`       | array   | 是   | 竞赛级别列表              |
| `description`  | string  | 是   | 竞赛描述                  |
| `website`      | string  | 是   | 竞赛官方网站URL           |
| `timeline`     | object  | 是   | 时间节点，包含`start_time`和`end_time` |
| `other_info`   | string  | 否   | 其他信息                  |

#### 请求示例

```json
{
  "name": "省级编程大赛",
  "types": ["编程", "技术"],
  "levels": ["省级"],
  "description": "这是一个面向省级学生的编程竞赛。",
  "website": "https://provincial_prog_competition.example.com",
  "timeline": {
    "start_time": "2024-06-01",
    "end_time": "2024-06-10"
  },
  "other_info": ""
}
```

#### 响应示例

- **成功（201 Created）**

```json
{
  "message": "竞赛投稿成功，等待管理员审核",
  "competition_id": 3
}
```

- **失败（400 Bad Request）**

```json
{
  "error": "缺少字段: name, types"
}
```

- **失败（500 Internal Server Error）**

```json
{
  "error": "竞赛投稿失败，请稍后重试"
}
```

---
