---
title: UCompositeTargetMethod
type: class
aliases: UCompositeTargetMethod
share: false

---

# UCompositeTargetMethod





Inherits from [UAbilityTargetMethod](/docs/SDK/Source/Classes/classUAbilityTargetMethod.md), [UTBLObject](/docs/SDK/Source/Classes/classUTBLObject.md), [UAssemblyObject](/docs/SDK/Source/Classes/classUAssemblyObject.md), UObject

Inherited by [UMultiTargetMethod](/docs/SDK/Source/Classes/classUMultiTargetMethod.md), [UProjectileTargetMethod](/docs/SDK/Source/Classes/classUProjectileTargetMethod.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[TargetUsingMethod]]**([UAbilityTargetMethod](/docs/SDK/Source/Classes/classUAbilityTargetMethod.md) * TargetMethod, const [FAbilityInitiationParams](/docs/SDK/Source/Classes/structFAbilityInitiationParams.md) & InInitiationParams, bool bLocal, int32 InMultiTargetMethodIndex) |
| | **[[UCompositeTargetMethod]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| TArray< [UAbilityTargetMethod](/docs/SDK/Source/Classes/classUAbilityTargetMethod.md) * > | **[[Children]]**  |
| TArray< [UAbilityTargetMethod](/docs/SDK/Source/Classes/classUAbilityTargetMethod.md) * > | **[[StaticChildren]]**  |
| bool | **[[bIgnoreChildrenInitiateRequirements]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| TArray< [UAbilityTargetMethod](/docs/SDK/Source/Classes/classUAbilityTargetMethod.md) * > | **[[DynamicChildren]]**  |
| TArray< [UAbilityTargetMethod](/docs/SDK/Source/Classes/classUAbilityTargetMethod.md) * > | **[[RunningChildren]]**  |
| bool | **[[bPendingFinish]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200