---
title: "Billing Overview"
type: concept
created: 2026-04-16
updated: 2026-04-16
tags:
  - billing
  - bss
status: seed
---

# Billing Overview

> BSS 计费系统概览，涵盖话单处理、批价、出账、收费等核心流程。

## 核心流程

1. **话单采集（CDR Collection）** — 从网络侧采集原始话单
2. **话单预处理（Pre-rating）** — 格式转换、去重、字段补齐
3. **批价（Rating）** — 根据资费规则计算费用
4. **出账（Invoicing）** — 汇总生成账单
5. **收费（Collection）** — 扣款、欠费管理
6. **对账（Reconciliation）** — 与财务系统对账

## 计费模式

- **预付费（Prepaid）** — 先充值后使用，实时扣费
- **后付费（Postpaid）** — 先使用后付费，按月出账
- **融合计费** — 预付费 + 后付费混合

## 待补充

- 批价引擎原理
- 漫游计费
- 5G 新计费（CHF、SBI）

