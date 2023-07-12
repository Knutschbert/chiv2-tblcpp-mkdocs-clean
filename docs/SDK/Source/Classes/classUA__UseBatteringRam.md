---
title: UA_UseBatteringRam
type: class
aliases: UA_UseBatteringRam
share: false

---

# UA_UseBatteringRam





Inherits from [UUtilityAI_Action](/docs/SDK/Source/Classes/classUUtilityAI__Action.md), UObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[UA_UseBatteringRam]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[OnChargeUpdated]]**([ABatteringRam](/docs/SDK/Source/Classes/classABatteringRam.md) * InBatteringRam, float Charge) |
| void | **[[OnDismount]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Driver, EDismountType DismountType) |
| void | **[[StartCharging]]**() |
| void | **[[StopCharging]]**() |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| [ABatteringRam](/docs/SDK/Source/Classes/classABatteringRam.md) * | **[[BatteringRam]]**  |
| AAIController * | **[[Controller]]**  |
| float | **[[DesiredChargePercent]]**  |
| [USiegeMountPoint](/docs/SDK/Source/Classes/classUSiegeMountPoint.md) * | **[[SiegeMountPoint]]**  |
| bool | **[[bCharging]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200