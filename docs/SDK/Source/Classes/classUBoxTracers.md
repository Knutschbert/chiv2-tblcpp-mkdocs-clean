---
title: UBoxTracers
type: class
aliases: UBoxTracers
share: false

---

# UBoxTracers





Inherits from [UTracerShape](/docs/SDK/Source/Classes/classUTracerShape.md), [UTBLObject](/docs/SDK/Source/Classes/classUTBLObject.md), [UAssemblyObject](/docs/SDK/Source/Classes/classUAssemblyObject.md), UObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[UBoxTracers]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| FName | **[[BoxComponentName]]**  |
| FVector | **[[CustomSocketExtents]]**  |
| FName | **[[CustomSocketName]]**  |
| int32 | **[[IgnoreParryDepth]]**  |
| bool | **[[bUseCustomSocket]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| UBoxComponent * | **[[BoxComponent]]**  |
| FVector | **[[BoxExtents]]**  |
| int32 | **[[CurrentIndex]]**  |
| FHitResult | **[[DelayHit]]**  |
| float | **[[DelayHitTime]]**  |
| FTransform | **[[LocalBoxTransform]]**  |
| TArray< FVector > | **[[TracerDirection]]**  |
| TArray< FTransform > | **[[TracerTransforms]]**  |
| bool | **[[bCanClash]]**  |
| bool | **[[bDelayedHit]]**  |
| bool | **[[bIsHorizontalBackSwingDone]]**  |
| bool | **[[bIsOverheadWindupDone]]**  |
| bool | **[[bIsStabWindupDone]]**  |
| bool | **[[bIsValid]]**  |
| bool | **[[bIsVerticalBackSwingDone]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200