---
title: UAbilityActivationMethod
type: class
aliases: UAbilityActivationMethod
share: false

---

# UAbilityActivationMethod





Inherits from [UTBLObject](/docs/SDK/Source/Classes/classUTBLObject.md), [UAssemblyObject](/docs/SDK/Source/Classes/classUAssemblyObject.md), UObject

Inherited by [UChannelingActivationMethod](/docs/SDK/Source/Classes/classUChannelingActivationMethod.md), [UCombatStateActivationMethod](/docs/SDK/Source/Classes/classUCombatStateActivationMethod.md), [UOnOffActivationMethod](/docs/SDK/Source/Classes/classUOnOffActivationMethod.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[UAbilityActivationMethod]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| TArray< [UAction](/docs/SDK/Source/Classes/classUAction.md) * > | **[[InitiatorActions]]**  |
| TArray< [UCondition](/docs/SDK/Source/Classes/classUCondition.md) * > | **[[InitiatorPrerequisites]]**  |
| uint8 | **[[bAllowSimultaneousInitiation]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| [UAbilitySpec](/docs/SDK/Source/Classes/classUAbilitySpec.md) * | **[[AbilitySpec]]**  |
| TWeakObjectPtr< AActor > | **[[Initiator]]**  |
| TWeakObjectPtr< [AAbilityInvocation](/docs/SDK/Source/Classes/classAAbilityInvocation.md) > | **[[Invocation]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200