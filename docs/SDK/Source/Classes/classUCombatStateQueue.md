---
title: UCombatStateQueue
type: class
aliases: UCombatStateQueue
share: false

---

# UCombatStateQueue





Inherits from UActorComponent

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[UCombatStateQueue]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[ClearHeldAttackQueue]]**() |
| void | **[[OnCancelGamepadTimeout]]**(float OverTime) |
| void | **[[OnComboCancelTimeout]]**(float OverTime) |
| void | **[[OnFeintQueueTimeout]]**(float OverTime) |
| void | **[[OnShowInGameMenu]]**() |
| void | **[[QueueFeint]]**(FName FeintAttack) |
| void | **[[ServerAddHeldInput]]**(FName InputActionName) |
| void | **[[ServerQueueInput]]**(FName NewQueuedInput) |
| void | **[[ServerQueueParry]]**() |
| void | **[[ServerRemoveHeldInput]]**(FName InputActionName) |
| void | **[[TryCancelAttack]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| TArray< FName > | **[[EarlyBlockStates]]**  |
| TArray< FName > | **[[ParryCounterQueueStates]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| TArray< [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) > | **[[AttackList]]**  |
| float | **[[CancelAttackPressedTime]]**  |
| int32 | **[[CancelGamepadTimer]]**  |
| float | **[[CancelIntoParryPressedTime]]**  |
| [UCombatStateComponent](/docs/SDK/Source/Classes/classUCombatStateComponent.md) * | **[[CombatStateComponent]]**  |
| [UCombatStateSynchronization](/docs/SDK/Source/Classes/classUCombatStateSynchronization.md) * | **[[CombatStateSynchronization]]**  |
| FName | **[[ComboCancelQueued]]**  |
| float | **[[ComboCancelTime]]**  |
| int32 | **[[ComboCancelTimer]]**  |
| TArray< FKey > | **[[ConsumedKeys]]**  |
| int32 | **[[FeintQueueTimer]]**  |
| float | **[[GamepadReloadPressedStartTime]]**  |
| TArray< FName > | **[[HeldInput]]**  |
| float | **[[HoldAttackQueueTime]]**  |
| FName | **[[HoldAttackQueued]]**  |
| TArray< [FInputPressedParams](/docs/SDK/Source/Classes/structFInputPressedParams.md) > | **[[InputQueue]]**  |
| float | **[[LastAltAttackPressedTime]]**  |
| float | **[[LastAltAttackTime]]**  |
| FName | **[[LastJumpInput]]**  |
| int32 | **[[PendingAttackId]]**  |
| [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) | **[[PendingParryCounterAttack]]**  |
| FName | **[[QueuedInput]]**  |
| TArray< FName > | **[[SendHeldInputToServer]]**  |
| float | **[[TimeSinceLastQueuedAttack]]**  |
| bool | **[[bAltAttack]]**  |
| bool | **[[bCanFeintSameAttackOnGamepad]]**  |
| bool | **[[bDisableSpecial]]**  |
| bool | **[[bDisableThrow]]**  |
| bool | **[[bFeintQueued]]**  |
| bool | **[[bFocusAttackHeld]]**  |
| bool | **[[bFocusHeld]]**  |
| bool | **[[bHoldAttack]]**  |
| bool | **[[bIsCancelAttackKeyDown]]**  |
| bool | **[[bIsCancelGamepadKeyDown]]**  |
| bool | **[[bIsCancelIntoParryKeyDown]]**  |
| bool | **[[bIsParryGamepadKeyDown]]**  |
| bool | **[[bParryQueued]]**  |
| bool | **[[bQueueHeldInputs]]**  |
| uint8 | **[[bShouldComboCancelQueue]]**  |
| bool | **[[bToggleAlt]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200