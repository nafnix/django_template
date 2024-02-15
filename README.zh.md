# Django 项目开发模板

这是一个 Django 4.2 项目的开发模板，此模板依赖 [PDM](https://pdm-project.org/)、[Redis](https://redis.io/) 与 [Postgres](https://www.postgresql.org/)，但带有的 devcontainer 中已经配置好了它们，使用 vscode 的 devcontainer 插件，你可以快速地在本地创建一个基于此模板的 Django 项目开发容器。

## 开发示例

## 部署示例

### 本地部署

```bash
cp .env.prod.example .env.prod
docker compose up
```

### 公网服务器上部署

若要在公网服务器上部署，注意要在 .env.prod 环境变量配置文件中修改相应的环境变量值，**必须** 修改的环境变量名称如下：

-   `DJANGO_SECRET_KEY`: Django 安全密钥
-   `DJANGO_STATIC_URL`: 静态文件地址

**建议** 修改的环境变量名称如下:

-   `PGADMIN_DEFAULT_EMAIL`: Pgadmin 的默认用户邮箱
-   `POSTGRES_PASSWORD`: 数据库密码
-   `DJANGO_ALLOWED_HOSTS`: 允许的主机名
