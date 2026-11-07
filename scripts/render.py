"""Render both language editions and the audit from curated project metadata."""
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = [
    ('student', 'Student Projects', '学生作品'),
    ('academic', 'Academic Resources', '学习资源'),
    ('campus', 'Campus Tools', '校园工具'),
    ('research', 'Research & Labs', '科研与实验室'),
    ('communities', 'Developer Communities', '开发者社区'),
    ('useful', 'Useful Resources', '实用资源'),
]

def activity(p, zh=False):
    if p['archived']:
        return '已归档' if zh else 'Archived'
    age = (date.fromisoformat(p['checked_on']) - date.fromisoformat(p['default_branch_commit_at'][:10])).days
    if age <= 180:
        return '180 天内有提交' if zh else 'Commit within 180 days'
    if age <= 365:
        return '181–365 天内有提交' if zh else 'Commit within 181–365 days'
    return '超过一年无提交' if zh else 'No commit within a year'

def render():
    projects = json.loads((ROOT / 'data/projects.json').read_text())
    files = {}
    for zh in [False, True]:
        filename = 'README.zh-CN.md' if zh else 'README.md'
        s = ['# Awesome CUHKSZ 🎓', '', '[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)', '', '[English](README.md) | 简体中文' if zh else 'English | [简体中文](README.zh-CN.md)', '']
        if zh:
            s += ['社区共同维护的香港中文大学（深圳）项目、开发工具、学习材料与实用资源索引。', '', '**CUHKSZ · CUHK-Shenzhen · CUHK(SZ) · LGU · 龙大 · 港中深**', '', '> 独立、非官方社区项目，与香港中文大学（深圳）无隶属关系，未获其背书。', '', '从能帮助一个同学的项目开始。欢迎新作品，不设 Star 门槛；学校关联须有公开依据，不推断个人身份。', '', '首批 **16 个项目**，数据核查于 **2026-11-01**。Star 是当日快照；活跃度按默认分支最近提交计算，分为 180 天内、181–365 天内和超过一年。这里的“近期”不代表持续维护承诺。', '', '**许可说明：** 列表同时索引开源软件和公开资源。“许可不明”仅表示未确认明确授权，不表示可自由复制、修改或分发。数据集、模型权重及第三方材料可能另有条款。', '', '查看[收录核查记录](docs/SELECTION.md)、[贡献指南](CONTRIBUTING.zh-CN.md)与[联系作者建议](docs/OUTREACH.md)。', '', '## 目录']
        else:
            s += ['A community-curated list of projects, developer tools, learning resources, and useful links related to The Chinese University of Hong Kong, Shenzhen.', '', '**CUHKSZ · CUHK-Shenzhen · CUHK(SZ) · LGU · 龙大 · 港中深**', '', '> An independent, unofficial community project. Not affiliated with or endorsed by CUHK-Shenzhen.', '', 'Start with something that helps a fellow student. New projects are welcome, with no star threshold. School connections require public evidence; personal identities are never inferred.', '', 'The initial **16 projects** were checked on **2026-11-01**. Stars are a dated snapshot. Activity uses the latest default-branch commit: within 180 days, 181–365 days, or over a year. Recent activity is not a promise of ongoing support.', '', '**Licensing:** This index includes open-source software and public resources. “License unclear” means explicit reuse permission has not been confirmed. Datasets, model weights, and third-party materials may carry separate terms.', '', 'See the [selection audit](docs/SELECTION.md), [contribution guide](CONTRIBUTING.md), and [author outreach guide](docs/OUTREACH.md).', '', '## Contents']
        s.append('')
        for category,en,cn in CATEGORIES:
            s.append(f'- [{cn if zh else en}](#{category})')
        s += ['- [参与贡献](#contributing)', '- [许可与声明](#license)'] if zh else ['- [Contributing](#contributing)', '- [License and disclaimer](#license)']
        for category,en,cn in CATEGORIES:
            s += ['', f'<a id="{category}"></a>', '', f'## {cn if zh else en}', '']
            if category == 'communities':
                if zh:
                    s += ['- [CUHK(SZ) Supercomputing Group](https://github.com/CUHKSZ-HPC) — 自述面向港中深学生的超算组织，提供研讨会与工具链材料。作为社区入口收录，不计入上述 16 个项目，也不宣称其当前活动频率。', '', '欢迎社区自荐；不公开非自愿提交的私人群链接。']
                else:
                    s += ['- [CUHK(SZ) Supercomputing Group](https://github.com/CUHKSZ-HPC) — A self-described student supercomputing organization with seminar and toolchain resources. Listed as a community entry, outside the 16-project count; no claim is made about current event activity.', '', 'Community submissions are welcome. Private group invitations require voluntary submission.']
            for p in sorted((p for p in projects if p['category']==category),key=lambda p:p['full_name'].lower()):
                name=p['full_name'].split('/')[1]
                lic=p['license'] or ('公开资源 · 许可不明' if zh else 'Public resource · license unclear')
                if p['full_name'].startswith('overdued/'):
                    lic='代码 MIT / 内容 CC BY 4.0' if zh else 'Code MIT / content CC BY 4.0'
                desc=p['summary_zh' if zh else 'summary_en']
                s.append(f"- [{name}]({p['html_url']}) — {desc} ⭐ {p['stargazers_count']}; {activity(p,zh)} ({p['default_branch_commit_at'][:10]}); {lic}.")
        if zh:
            s += ['', '<a id="contributing"></a>', '', '## 参与贡献', '', '欢迎通过 Issue 推荐资源，或按[贡献指南](CONTRIBUTING.zh-CN.md)提交 PR。自荐请说明关系，提供公开关联依据，并保持双语简介一致。', '', '请遵守[行为准则](CODE_OF_CONDUCT.zh-CN.md)。更正、失效链接及移除请求同样欢迎；收录不表示作者已接受邀请或加入维护团队。', '', '<a id="license"></a>', '', '## 许可与声明', '', '本仓库原创内容采用 [MIT](LICENSE)，中文解释见[维护说明](docs/MAINTAINING.md)。被链接项目及第三方内容保留各自许可。', '', '校园指南与课程记录可能过时；转学分结果以学校审批为准。项目、课程与实验室名称仅用于识别，不代表学校或作者背书。', '', '组织方式参考 [Awesome](https://github.com/sindresorhus/awesome) 与大学社区资源项目；[参考来源](docs/REFERENCES.md)记录具体借鉴方式。本列表尚未声称被官方 Awesome 目录收录。']
        else:
            s += ['', '<a id="contributing"></a>', '', '## Contributing', '', 'Suggest a resource through an issue or submit a PR using the [contribution guide](CONTRIBUTING.md). Disclose self-submissions, provide public affiliation evidence, and keep both language editions consistent.', '', 'Please follow the [Code of Conduct](CODE_OF_CONDUCT.md). Corrections, broken-link reports, and removal requests are welcome. Listing does not mean an author accepted an invitation or joined the maintenance team.', '', '<a id="license"></a>', '', '## License and disclaimer', '', 'Original repository content is available under [MIT](LICENSE). See [maintenance notes](docs/MAINTAINING.md) for scope. Linked projects and third-party materials retain their own terms.', '', 'Campus guidance and course records can become outdated; credit transfers remain subject to university approval. Project, course, and lab names identify resources without implying institutional or author endorsement.', '', 'Structure draws on [Awesome](https://github.com/sindresorhus/awesome) and university community resources; see [editorial references](docs/REFERENCES.md). This list does not claim acceptance into the upstream Awesome directory.']
        files[filename]='\n'.join(s)+'\n'
    s=['# Selection audit / 收录核查', '', 'Snapshot / 核查日期：2026-11-01。16 projects / 16 个项目。', '', 'Ordered by stars for this audit only; README categories use alphabetical order. Dates are UTC commit dates. All selected repositories were unarchived at observation. / 本表仅为核查按 Star 排序；README 分类内按字母排序。日期为 UTC 提交日期，核查时全部未归档。', '', '| Repository / 仓库 | Stars | Default-branch commit / 默认分支提交 | Activity / 活跃度 | License / 许可 |', '| --- | ---: | --- | --- | --- |']
    for p in sorted(projects,key=lambda p:p['stargazers_count'],reverse=True):
        s.append(f"| [{p['full_name']}]({p['html_url']}) | {p['stargazers_count']} | [{p['default_branch_commit_at'][:10]}]({p['commit_url']}) | {activity(p)} / {activity(p,True)} | {p['license'] or 'Unclear / 不明'} |")
    recent=sum(activity(p)=='Commit within 180 days' for p in projects)
    s += ['', f'**{recent}/16** have a default-branch commit within 180 days; **{16-recent}/16** fall within 181–365 days. / **{recent}/16** 在 180 天内有默认分支提交，其余 **{16-recent}/16** 在 181–365 天内。', '', 'Campus projects have smaller audiences; the initial selection prioritizes local usefulness alongside stars. Amphion, TwinMarket, DualCodec, and CSC4005 are retained as established resources and are not labeled active within 180 days. / 校园项目受众较小，首批兼顾实用性与关注度；Amphion、TwinMarket、DualCodec 与 CSC4005 保留为已有积累的资源，不称为 180 天内活跃。', '', '## Public connection evidence / 公开关联依据', '']
    for p in sorted(projects,key=lambda p:p['full_name'].lower()):
        s += [f"- [{p['full_name']}]({p['evidence_url']}) — {p['affiliation_note']}"]
        if p.get('license_note'):s.append('  '+p['license_note'])
    s += ['', 'All contact statuses are `not_contacted`. The author’s NeuroTrip and weblog are self-nominated and receive the same license and activity labels as other entries. / 联系状态全部为未联系；作者自荐的 NeuroTrip 与 weblog 使用相同许可和活跃度标准。', '', 'High-star historical candidates such as archived netdisk utilities and older homework collections were not used to inflate the selection. The LGU keyword also returned Lahore Garrison University projects, which were excluded. / 未用归档网盘工具或旧作业集凑高 Star 项目数；LGU 搜索中出现的 Lahore Garrison University 项目已排除。', '', 'See [methodology and references](REFERENCES.md) and [outreach templates](OUTREACH.md).']
    files['docs/SELECTION.md']='\n'.join(s)+'\n'
    return files

if __name__ == '__main__':
    for name, content in render().items():
        (ROOT / name).write_text(content)
    print('Rendered English, Chinese, and selection audit.')
