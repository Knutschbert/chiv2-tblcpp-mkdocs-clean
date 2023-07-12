---
title: UAnimationSet
type: class
aliases: UAnimationSet
share: false

---

# UAnimationSet





Inherits from [UTBLObject](/docs/SDK/Source/Classes/classUTBLObject.md), [UAssemblyObject](/docs/SDK/Source/Classes/classUAssemblyObject.md), UObject

Inherited by [UNativeAnimationSet_Base](/docs/SDK/Source/Classes/classUNativeAnimationSet__Base.md), [UNativeAnimationSet_BaseMount](/docs/SDK/Source/Classes/classUNativeAnimationSet__BaseMount.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[UAnimationSet]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| bool | **[[bIsCustomization]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| TArray< [FTracerCacheKey](/docs/SDK/Source/Classes/structFTracerCacheKey.md) > | **[[AdditionalTracerCacheKeys]]**  |
| int32 | **[[AnimationFPS]]**  |
| TMap< FString, FString > | **[[AutoMapAnimations]]**  |
| FString | **[[CharacterSet]]**  |
| TArray< [FTracerCacheKey](/docs/SDK/Source/Classes/structFTracerCacheKey.md) > | **[[DefaultTracerCacheKeys]]**  |
| TMap< [FTracerCacheKey](/docs/SDK/Source/Classes/structFTracerCacheKey.md), [FTracerCache](/docs/SDK/Source/Classes/structFTracerCache.md) > | **[[TracerCache]]**  |
| TArray< UAnimMontage * > | **[[TracerMontages]]**  |
| TArray< UAnimSequenceBase * > | **[[TracerSequences]]**  |
| FString | **[[WeaponSet]]**  |
| bool | **[[bFirstPerson]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200