# LLM4Rec — 多目标数据选择、互补学习与证据获取

新增研究专题，位于Research根目录，与crystal平级。本包没有修改原README、crystal或其他原有文件。

[完整汇编](docs/FULL_REPORT_ZH.md) · [主报告](docs/RESEARCH_REPORT_ZH.md) · [十个方向](docs/ideas/README.md) · [实际验证](docs/VALIDATION.md) · [自审记录](docs/AUDIT.md) · [49项来源](references/README.md) · [结构化论文索引](bibliography/papers.json)

**110项CPU测试通过不是十个方法真实有效。tiny SFT未稳定改善，atoms未显示额外价值；真实LLM/业务/科学执行实验没有完成。** 来源卡标明L0/L0+阅读层级，没有把摘要核验改名全文审计。

配套实施目标为YWDDLiang/rec，用户自行上传。本文档中的训练和测试命令在随附rec实施仓库运行，不是在本研究资料目录运行。本目录仅提供独立资料校验：

```bash
python llm4rec/scripts/validate_repo.py
```

若要在Research根README增加导航，手动追加指向`./llm4rec/README.md`的链接即可。不要用本包替换整个Research仓库。导师框架读取版本为299bd85752ce1a59ea5cce8c1b145777e33cba6f，来源与公式边界说明保留于docs/provenance和landscape。

所有结果和合成示例仅用于复现数学/工程判断；公开前请确认PPT提取文字的发布授权。
