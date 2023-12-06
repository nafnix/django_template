# Django Project Development Template

[中文版](./README.zh.md)

This is a development template for a Django 4.2 project. The template relies on [PDM](https://pdm-project.org/), [Redis](https://redis.io/), and [Postgres](https://www.postgresql.org/). However, these dependencies are pre-configured in the devcontainer provided. By using the vscode devcontainer plugin, you can quickly create a local development container based on this template.

## Deployment Example

### Local Deployment

```bash
cp .env.prod.example .env.prod
docker compose up
```

### Deployment on a Public Server

If you want to deploy on a public server, make sure to modify the corresponding environment variable values in the .env.prod environment configuration file. **Mandatory** environment variables that must be modified are as follows:

- `PGADMIN_DEFAULT_PASSWORD`: Default password for Pgadmin
- `DJANGO_SECRET_KEY`: Django security key
- `DJANGO_STATIC_URL`: URL for static files

**Recommended** environment variables to modify are as follows:

- `PGADMIN_DEFAULT_EMAIL`: Default email for Pgadmin user
- `POSTGRES_PASSWORD`: Database password
- `DJANGO_ALLOWED_HOSTS`: Allowed hostnames
