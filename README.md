# One 竞赛

## 开发中……

(dev)在线查看：[https://one-competition.pages.dev/](https://one-competition.pages.dev/)

## 前端部署

需要先安装 Node.js 和 pnpm。

安装依赖

```bash
cd frontend
pnpm install
```

开发模式

```bash
pnpm run dev
```

## 后端部署

数据库，按照`settings.py`要求，用户名为`root`, 密码`123456789`，数据库名称`one_competition`

```bash
cd backend
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
(如果发现migrate有问题，尝试命令`python manage.py migrate competition 0003_user`似乎有奇效)
