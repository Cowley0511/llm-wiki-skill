---
title: "BSS Architecture Overview"
type: concept
created: 2026-04-16
updated: 2026-04-16
tags:
  - architecture
  - oss-bss
status: seed
---

# BSS Architecture Overview

> BSS（Business Support System，业务支撑系统）整体架构总览。

## 定义

BSS 是电信运营商 IT 系统的核心组成部分，与 OSS（Operations Support System）共同构成 OSS/BSS 体系。

## 核心子域

- [[Billing Overview|计费系统]] — 话单处理、批价、出账、收费
- [[CRM System|客户关系管理]] — 客户管理、订单受理、服务保障
- [[Order Management|订单管理]] — 订单分解、服务开通
- [[Product Management|产品管理]] — 产品目录、资费管理、促销
- [[Revenue Management|收入管理]] — 收入确认、财务对账、报表

## 与 OSS 的关系

- BSS 面向市场和客户（To-C / To-B）
- OSS 面向网络和运维（Network & IT Operations）
- 边界：BSS 处理商业逻辑，OSS 处理网络开通和故障

## 待补充

- BSS 演进历程（从传统架构到云原生）
- 典型部署架构图
- 与 OSS 的接口标准

