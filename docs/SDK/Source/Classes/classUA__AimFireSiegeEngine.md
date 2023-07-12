---
title: UA_AimFireSiegeEngine
type: class
aliases: UA_AimFireSiegeEngine
share: false

---

# UA_AimFireSiegeEngine





Inherits from [UUtilityAI_Action](/docs/SDK/Source/Classes/classUUtilityAI__Action.md), UObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[UA_AimFireSiegeEngine]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[EndAction]]**() |
| void | **[[Fire]]**() |
| void | **[[OnDismount]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Driver, EDismountType DismountType) |
| void | **[[TryAim]]**() |
| void | **[[TryCharge]]**() |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| FTimerHandle | **[[ActionTimerHandle]]**  |
| uint8 | **[[AdjustmentCount]]**  |
| FInt32Range | **[[AdjustmentRange]]**  |
| float | **[[AimEndTime]]**  |
| FVector2D | **[[AimTimeRange]]**  |
| TWeakObjectPtr< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > | **[[Character]]**  |
| FVector2D | **[[ChargeRange]]**  |
| TWeakObjectPtr< AAIController > | **[[Controller]]**  |
| FVector2D | **[[CurrentInput]]**  |
| TWeakObjectPtr< [ASiegeEngine](/docs/SDK/Source/Classes/classASiegeEngine.md) > | **[[CurrentSiegeEngine]]**  |
| uint8 | **[[MaxAdjustments]]**  |
| float | **[[NextRecalculateTime]]**  |
| float | **[[RandomCharge]]**  |
| bool | **[[bCanBeCharged]]**  |
| bool | **[[bIsFiring]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200