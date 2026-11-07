# Maintaining / 维护说明

English: Run `python3 scripts/render.py` after editing `data/projects.json`, then `python3 scripts/check.py`. Read the actual README and license before changing a status. Quarterly, refresh public GitHub metadata and the latest default-branch commit, check affiliation evidence and links, then review the resulting diff. Never automate outreach or remove projects solely because stars fell or commits stopped. Workflows check local structure on PRs; the monthly link job reports failures for human review and cannot prove a linked application works.

中文：编辑数据后运行生成与检查脚本。修改状态前阅读实际 README 和许可。每季度刷新 GitHub 公开元数据与默认分支最新提交，复核关联证据和链接，再审查差异。不自动联系作者，不因 Star 减少或停止提交而直接移除项目。PR 工作流检查本地结构；每月链接任务仅报告需人工复核的失败，不能证明网站功能正常。

## Launch / 发布

Use `awesome-cuhksz` as the GitHub repository name. Suggested description: “A community-curated list of projects, developer tools, learning resources, and useful links related to CUHK-Shenzhen.” Suggested topics: `awesome`, `awesome-list`, `cuhksz`, `cuhk-shenzhen`, `campus`, `student-projects`.

建议 GitHub 仓库名为 `awesome-cuhksz`，介绍采用上文英文句子，Topics 使用上列关键词。LGU、龙大、港中深作为 README 检索别名，不将 LGU 单独当作学校身份依据。

The local folder is independent of the final GitHub slug. Publish this prepared content through your normal GitHub workflow, then use actual links in outreach messages. Do not claim a remote URL exists before publication. Enable Issues and, if useful, Discussions. Establish a private reporting contact on the owner’s public profile before inviting a wider community. Create `good first issue` labels and focused tasks such as checking one description or translating one entry. A second maintainer should join by explicit agreement, with least necessary repository permissions.

本地目录名与最终 GitHub 名称独立。通过正常 GitHub 流程发布后，再将真实链接填入邀请模板；发布前不声称远端已存在。开启 Issues，按需开启 Discussions。在邀请更广泛社区前，在所有者公开主页建立私密反馈联系方式。创建 `good first issue` 标签，安排核对一个描述或翻译一个条目等具体任务。邀请第二位维护者时须明确征得同意，并只授予必要权限。

## License / 许可

Original text, metadata arrangement, and scripts in this repository use MIT. The English LICENSE is the operative text; the Chinese explanation is informational: you may use, modify, and redistribute the repository’s original materials while retaining the copyright and permission notice; no warranty is provided. Linked resources, university names, logos, datasets, weights, and third-party content are not relicensed by this repository.

本仓库原创文字、元数据编排和脚本采用 MIT，英文 LICENSE 为许可文本。中文说明：保留版权与许可声明后，可使用、修改及分发本仓库原创材料，不提供担保。被链接资源、学校名称、标识、数据集、权重与第三方内容不因被收录而改用 MIT。
