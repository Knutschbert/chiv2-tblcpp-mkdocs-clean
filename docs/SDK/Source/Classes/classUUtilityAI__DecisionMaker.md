---
title: UUtilityAI_DecisionMaker
type: class
aliases: UUtilityAI_DecisionMaker
share: false

---

# UUtilityAI_DecisionMaker





Inherits from UActorComponent

Inherited by [UUtilityAI_CombatDecisionMaker](/docs/SDK/Source/Classes/classUUtilityAI__CombatDecisionMaker.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[UUtilityAI_DecisionMaker]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| TArray< TSubclassOf< [UUtilityAI_BehaviorSet](/docs/SDK/Source/Classes/classUUtilityAI__BehaviorSet.md) > > | **[[BehaviorSets]]**  |
| TArray< [UUtilityAI_Behavior](/docs/SDK/Source/Classes/classUUtilityAI__Behavior.md) * > | **[[Behaviors]]**  |
| TMap< TSubclassOf< [UUtilityAI_Behavior](/docs/SDK/Source/Classes/classUUtilityAI__Behavior.md) >, [UUtilityAI_Behavior](/docs/SDK/Source/Classes/classUUtilityAI__Behavior.md) * > | **[[BehaviorsByClass]]**  |
| UBlackboardData * | **[[BlackboardAsset]]**  |
| [FUtilityAI_Decision](/docs/SDK/Source/Classes/structFUtilityAI__Decision.md) | **[[DecisionPendingDisengage]]**  |
| [FUtilityAI_Decision](/docs/SDK/Source/Classes/structFUtilityAI__Decision.md) | **[[LastDecision]]**  |
| TArray< [FUtilityAI_Decision](/docs/SDK/Source/Classes/structFUtilityAI__Decision.md) > | **[[LastDecisions]]**  |
| TMap< TSubclassOf< [UUtilityAI_Behavior](/docs/SDK/Source/Classes/classUUtilityAI__Behavior.md) >, float > | **[[LastTimeBehaviorChosen]]**  |
| EStaggeredUpdateCategory | **[[UpdateCategory]]**  |
| bool | **[[bHasInitialized]]**  |
| bool | **[[bIsCombatDecisionMaker]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| TSet< [FBehaviorSetOverride](/docs/SDK/Source/Classes/structFBehaviorSetOverride.md) > | **[[BehaviorOverrides]]**  |
| [FBehaviorSetOverride](/docs/SDK/Source/Classes/structFBehaviorSetOverride.md) | **[[ForcedBehaviorSet]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:01 +0200