---
title: UTriggeredAction
type: class
aliases: UTriggeredAction
share: false

---

# UTriggeredAction





Inherits from [UAction](/docs/SDK/Source/Classes/classUAction.md), [UTBLObject](/docs/SDK/Source/Classes/classUTBLObject.md), [UAssemblyObject](/docs/SDK/Source/Classes/classUAssemblyObject.md), UObject

Inherited by [UEventCombatStateChanged](/docs/SDK/Source/Classes/classUEventCombatStateChanged.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[OnInvocationComplete]]**([AAbilityInvocation](/docs/SDK/Source/Classes/classAAbilityInvocation.md) * Invocation, [UAbilitySpec](/docs/SDK/Source/Classes/classUAbilitySpec.md) * AbilitySpec) |
| | **[[UTriggeredAction]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| TArray< [UAction](/docs/SDK/Source/Classes/classUAction.md) * > | **[[Actions]]**  |
| uint8 | **[[bIgnoreTerminate]]**  |
| uint8 | **[[bTriggerMustOccur]]**  |
| uint8 | **[[bTriggerOnce]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| TWeakObjectPtr< AActor > | **[[TargetActor]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:01 +0200