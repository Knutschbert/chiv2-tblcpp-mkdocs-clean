---
title: UUtilityAI_Action
type: class
aliases: UUtilityAI_Action
share: false

---

# UUtilityAI_Action





Inherits from UObject

Inherited by [UA_AimFireSiegeEngine](/docs/SDK/Source/Classes/classUA__AimFireSiegeEngine.md), [UA_ChargeSiegeEngine](/docs/SDK/Source/Classes/classUA__ChargeSiegeEngine.md), [UA_DismountSiegeEngine](/docs/SDK/Source/Classes/classUA__DismountSiegeEngine.md), [UA_EnterCombatWith](/docs/SDK/Source/Classes/classUA__EnterCombatWith.md), [UA_MaintainDistanceFromActor](/docs/SDK/Source/Classes/classUA__MaintainDistanceFromActor.md), [UA_SetBlackboardValueToContextTarget](/docs/SDK/Source/Classes/classUA__SetBlackboardValueToContextTarget.md), [UA_UseBatteringRam](/docs/SDK/Source/Classes/classUA__UseBatteringRam.md), [UA_UseCharacterMountableActor](/docs/SDK/Source/Classes/classUA__UseCharacterMountableActor.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| bool | **[[IsDoneOrCanInterrupt]]**() const |
| bool | **[[IsInProgress]]**() const |
| void | **[[SetCanInterrupt]]**(bool bInCanInterrupt) |
| bool | **[[ShouldRestartIfRedecidedUpon]]**() const |
| void | **[[TickAction]]**(float DeltaTime, [FUtilityAI_Context](/docs/SDK/Source/Classes/structFUtilityAI__Context.md) C) |
| | **[[UUtilityAI_Action]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[CompleteAction]]**(const [FUtilityAI_Context](/docs/SDK/Source/Classes/structFUtilityAI__Context.md) & C) |
| void | **[[MarkFinished]]**() |
| void | **[[MarkReadyToFinish]]**() |
| void | **[[PerformAction]]**(const [FUtilityAI_Context](/docs/SDK/Source/Classes/structFUtilityAI__Context.md) & C) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| FOnUtilityAIActionDone | **[[OnDone]]**  |
| EActionPriorityLevel | **[[PriorityLevel]]**  |
| bool | **[[bCanInterrupt]]**  |
| bool | **[[bIsInProgress]]**  |
| bool | **[[bIsReadyToComplete]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| bool | **[[bDoNotRestartIfRedecidedUpon]]**  |
| bool | **[[bLatentAction]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:01 +0200