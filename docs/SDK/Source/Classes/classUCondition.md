---
title: UCondition
type: class
aliases: UCondition
share: false

---

# UCondition





Inherits from [UTBLObject](/docs/SDK/Source/Classes/classUTBLObject.md), [UAssemblyObject](/docs/SDK/Source/Classes/classUAssemblyObject.md), UObject

Inherited by [UCanDash](/docs/SDK/Source/Classes/classUCanDash.md), [UCanDropItem](/docs/SDK/Source/Classes/classUCanDropItem.md), [UCanJump](/docs/SDK/Source/Classes/classUCanJump.md), [UCanSwitchInventoryItem](/docs/SDK/Source/Classes/classUCanSwitchInventoryItem.md), [UCanUseItem](/docs/SDK/Source/Classes/classUCanUseItem.md), [UIsActiveRiposte](/docs/SDK/Source/Classes/classUIsActiveRiposte.md), [UIsAlive](/docs/SDK/Source/Classes/classUIsAlive.md), [UIsAttackType](/docs/SDK/Source/Classes/classUIsAttackType.md), [UIsCombatState](/docs/SDK/Source/Classes/classUIsCombatState.md), [UIsCounter](/docs/SDK/Source/Classes/classUIsCounter.md), [UIsCounterSuccess](/docs/SDK/Source/Classes/classUIsCounterSuccess.md), [UIsCrouched](/docs/SDK/Source/Classes/classUIsCrouched.md), [UIsEnemy](/docs/SDK/Source/Classes/classUIsEnemy.md), [UIsHorseMovementState](/docs/SDK/Source/Classes/classUIsHorseMovementState.md), [UIsLookingDown](/docs/SDK/Source/Classes/classUIsLookingDown.md), [UIsMovementDirection](/docs/SDK/Source/Classes/classUIsMovementDirection.md), [UIsMovementMode](/docs/SDK/Source/Classes/classUIsMovementMode.md), [UIsMoving](/docs/SDK/Source/Classes/classUIsMoving.md), [UIsNot](/docs/SDK/Source/Classes/classUIsNot.md), [UIsRiposte](/docs/SDK/Source/Classes/classUIsRiposte.md), [UIsSelf](/docs/SDK/Source/Classes/classUIsSelf.md), [UIsStat](/docs/SDK/Source/Classes/classUIsStat.md), [UIsType](/docs/SDK/Source/Classes/classUIsType.md), [UOrCondition](/docs/SDK/Source/Classes/classUOrCondition.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[UCondition]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| bool | **[[bLogEvents]]**  |
| bool | **[[bTreatInitiatorAsTarget]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| [FActionContext](/docs/SDK/Source/Classes/structFActionContext.md) | **[[Context]]**  |
| TWeakObjectPtr< UObject > | **[[Initiator]]**  |
| TWeakObjectPtr< UObject > | **[[Target]]**  |
| FVector | **[[TargetLocation]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200