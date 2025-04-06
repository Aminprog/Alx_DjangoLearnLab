# Social Media API 🧑‍🤝‍🧑

A beginner-friendly Django REST API project with token-based user authentication.

---

## Features

- Custom user model
- Token authentication
- User registration
- Login (returns auth token)
- Profile view/update (requires token)
- Followers (ManyToMany)

---

## Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab/social_media_api

## Posts & Comments Endpoints

### 1. Posts
- **GET** `/api/posts/` : List all posts (paginated)
  - Supports search with `?search=keyword`
  - Example: `GET /api/posts/?search=hello`
- **POST** `/api/posts/` : Create new post (requires token)
  - Body: `{ "title": "...", "content": "..." }`
- **GET** `/api/posts/{id}/` : Retrieve a single post
- **PUT** `/api/posts/{id}/` : Update post (author only)
- **DELETE** `/api/posts/{id}/` : Delete post (author only)

### 2. Comments
- **GET** `/api/comments/` : List all comments (paginated)
- **POST** `/api/comments/` : Create new comment (requires token)
  - Body: `{ "post": 1, "content": "..." }`
- **GET** `/api/comments/{id}/` : Retrieve a single comment
- **PUT** `/api/comments/{id}/` : Update comment (author only)
- **DELETE** `/api/comments/{id}/` : Delete comment (author only)

**Headers**:  
- `Authorization: Token <your_token_here>` for all authenticated requests.

