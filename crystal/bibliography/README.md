# Bibliography data

> [返回晶体索引](../README.md)

- `papers.json`：完整机器可读元数据和审计字段；
- `paper-index.csv`：便于筛选、排序和外部导入；
- 单篇详细报告位于 `../papers/<slug>.md`。

## 字段说明

| 字段 | 含义 |
|---|---|
| `slug` | 稳定文件标识 |
| `group` | 本库问题簇 |
| `category` | 论文自己的任务/方法类别 |
| `role` | 去故事化后的首轮角色判断 |
| `problem`–`verdict` | 十二项论文审计的结构化字段 |
| `scores` | \([\Delta P,\Delta I,\Delta O,\Delta C,\Delta E,\Delta K]\) |
| `project_verified` | 当前是否已核验到官方/作者项目地址 |
| `last_verified` | 元数据最后核验日期 |

`project_verified=false` 不等于论文没有代码，只表示本库尚未把项目地址核验到主索引。
