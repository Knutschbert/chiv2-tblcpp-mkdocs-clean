---
title: UA_UseCharacterMountableActor
type: class
aliases: UA_UseCharacterMountableActor
share: false

---

# UA_UseCharacterMountableActor





Inherits from [UUtilityAI_Action](/docs/SDK/Source/Classes/classUUtilityAI__Action.md), UObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[UA_UseCharacterMountableActor]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[OnChargeUpdated]]**([ACharacterMountableActor](/docs/SDK/Source/Classes/classACharacterMountableActor.md) * InCharacterMountableActor, float Charge) |
| void | **[[OnDismount]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Driver, EDismountType DismountType) |
| void | **[[StartCharging]]**() |
| void | **[[StopCharging]]**() |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| [ACharacterMountableActor](/docs/SDK/Source/Classes/classACharacterMountableActor.md) * | **[[CharacterMountableActor]]**  |
| AAIController * | **[[Controller]]**  |
| float | **[[DesiredChargePercent]]**  |
| [USiegeMountPoint](/docs/SDK/Source/Classes/classUSiegeMountPoint.md) * | **[[SiegeMountPoint]]**  |
| bool | **[[bCharging]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200