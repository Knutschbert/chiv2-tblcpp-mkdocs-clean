---
title: UCombatStateSynchronization
type: class
aliases: UCombatStateSynchronization
share: false

---

# UCombatStateSynchronization





Inherits from UActorComponent

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[UCombatStateSynchronization]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[ClientOnAttackFailed]]**(int32 AttackID) |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| TArray< [FSyncAttackId](/docs/SDK/Source/Classes/structFSyncAttackId.md) > | **[[CancelledAttacks]]**  |
| [UCombatStateComponent](/docs/SDK/Source/Classes/classUCombatStateComponent.md) * | **[[CombatStateComponent]]**  |
| [UCombatStateQueue](/docs/SDK/Source/Classes/classUCombatStateQueue.md) * | **[[CombatStateQueue]]**  |
| TArray< [FSyncAttackId](/docs/SDK/Source/Classes/structFSyncAttackId.md) > | **[[FailedAttacks]]**  |
| [FFailedAttackInfo](/docs/SDK/Source/Classes/structFFailedAttackInfo.md) | **[[LastFailedAttack]]**  |
| int32 | **[[LatestAttackID]]**  |
| TArray< [FSyncAttackId](/docs/SDK/Source/Classes/structFSyncAttackId.md) > | **[[ReceivedAcks]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200