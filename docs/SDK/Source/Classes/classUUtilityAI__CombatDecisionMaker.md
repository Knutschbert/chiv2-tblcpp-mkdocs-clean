---
title: UUtilityAI_CombatDecisionMaker
type: class
aliases: UUtilityAI_CombatDecisionMaker
share: false

---

# UUtilityAI_CombatDecisionMaker





Inherits from [UUtilityAI_DecisionMaker](/docs/SDK/Source/Classes/classUUtilityAI__DecisionMaker.md), UActorComponent

## Public Functions

|                | Name           |
| -------------- | -------------- |
| [FIncomingAttackInfo](/docs/SDK/Source/Classes/structFIncomingAttackInfo.md) | **[[GetIncomingAttackInfo]]**() const |
| | **[[UUtilityAI_CombatDecisionMaker]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [FCombatEventBehaviors](/docs/SDK/Source/Classes/structFCombatEventBehaviors.md) | **[[Blocked_BehaviorSet]]**  |
| [FCombatEventBehaviors](/docs/SDK/Source/Classes/structFCombatEventBehaviors.md) | **[[DamageCaused_BehaviorSet]]**  |
| [FCombatEventBehaviors](/docs/SDK/Source/Classes/structFCombatEventBehaviors.md) | **[[EnemyBlockedMyHit_BehaviorSet]]**  |
| [FCombatEventBehaviors](/docs/SDK/Source/Classes/structFCombatEventBehaviors.md) | **[[EnemyEnteredCC_BehaviorSet]]**  |
| FTimerHandle | **[[HandleAttackTimer]]**  |
| FTimerHandle | **[[HandleParryTimer]]**  |
| [FCombatEventBehaviors](/docs/SDK/Source/Classes/structFCombatEventBehaviors.md) | **[[IncomingAttack_BehaviorSet]]**  |
| [FCombatEventBehaviors](/docs/SDK/Source/Classes/structFCombatEventBehaviors.md) | **[[IncomingCombatStateChange_BehaviorSet]]**  |
| [FCombatEventBehaviors](/docs/SDK/Source/Classes/structFCombatEventBehaviors.md) | **[[IncomingShove_BehaviorSet]]**  |
| [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * | **[[OverrideDecisionActor]]**  |
| [FCombatEventBehaviors](/docs/SDK/Source/Classes/structFCombatEventBehaviors.md) | **[[ParrySuccess_BehaviorSet]]**  |
| [FCombatEventBehaviors](/docs/SDK/Source/Classes/structFCombatEventBehaviors.md) | **[[Recovery_BehaviorSet]]**  |
| [FCombatEventBehaviors](/docs/SDK/Source/Classes/structFCombatEventBehaviors.md) | **[[Thwacked_BehaviorSet]]**  |
| [FCombatEventBehaviors](/docs/SDK/Source/Classes/structFCombatEventBehaviors.md) | **[[TookDamage_BehaviorSet]]**  |
| bool | **[[bShouldRecieveAllCombatStateChanges]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:01 +0200