# GitHub Actions 配置

项目包含两个会写回仓库的自动化工作流：

- `.github/workflows/arxiv_bot.yml`：工作日 05:40 UTC 更新主 README 和 AI 摘要缓存。
- `.github/workflows/update-conferences.yml`：工作日 06:00 UTC 更新会议 README 和缓存。

两个工作流共享 `paper-updates-${{ github.ref }}` 并发组，避免同时提交生成文件。

## 仓库权限

进入 `Settings -> Actions -> General -> Workflow permissions`，选择：

```text
Read and write permissions
```

工作流本身只声明 `contents: write`，不需要 Pull Request 写权限。

## AI 摘要密钥

主机器人启用 AI 摘要时，需要在 `Settings -> Secrets and variables -> Actions`
中创建：

```text
ARK_API_KEY
```

没有该密钥时，论文抓取和 README 生成仍可运行，但不会为未命中缓存的论文生成新摘要。

## 测试门禁

生成内容前会执行：

```bash
pytest --cov=arxiv_bot --cov=base_conference_bot --cov=run_all_bots --cov-fail-under=50
```

测试失败、覆盖率不足、全部上游数据源失败或任一会议机器人失败时，工作流不会提交生成文件。

## 手动运行

在 Actions 页面选择对应工作流并点击 `Run workflow`。

会议工作流支持：

```text
all
arch,hpc,sys
ai,iclr
```

## 分支行为

工作流使用 `${GITHUB_REF_NAME}` 拉取和推送当前触发分支，同时支持 `main` 和 `master`，
不再硬编码目标分支。

## 常见问题

- 推送被拒绝：确认 Workflow permissions 已设为可写，并检查是否有分支保护规则。
- AI 摘要缺失：确认 `ARK_API_KEY` 存在，并检查模型 API 日志。
- 会议缓存未更新：查看日志中的失败数据源；旧缓存会保留，避免被空结果覆盖。
- 覆盖率失败：先在本地运行同一条 pytest 命令，再提交测试与实现。
