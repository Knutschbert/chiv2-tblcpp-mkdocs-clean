---
title: USphereTargetMethod
type: class
aliases: USphereTargetMethod
share: false

---

# USphereTargetMethod





Inherits from [UShapeTargetMethod](/docs/SDK/Source/Classes/classUShapeTargetMethod.md), [UAbilityTargetMethod](/docs/SDK/Source/Classes/classUAbilityTargetMethod.md), [UTBLObject](/docs/SDK/Source/Classes/classUTBLObject.md), [UAssemblyObject](/docs/SDK/Source/Classes/classUAssemblyObject.md), UObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[DelayFinish]]**() |
| void | **[[GetSphereCenter]]**(FVector & SphereCenter, FTransform & ControllerTransform) |
| | **[[USphereTargetMethod]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| TEnumAsByte< ETargetVisibilityCheck::Type > | **[[CheckVisibility]]**  |
| float | **[[DelayFinishTime]]**  |
| float | **[[MaxRange]]**  |
| int32 | **[[MaxTargets]]**  |
| ESphereHitDirection | **[[SphereHitDirection]]**  |
| FVector | **[[SphereOffset]]**  |
| float | **[[SphereRadius]]**  |
| TEnumAsByte< ECollisionChannel > | **[[TargetChannel]]**  |
| float | **[[ZDownLimiter]]**  |
| float | **[[ZUpLimiter]]**  |
| bool | **[[bTargetSelf]]**  |
| bool | **[[bUseControllerRotation]]**  |
| bool | **[[bUseMountRotation]]**  |
| bool | **[[bUseTargetChannel]]**  |
| bool | **[[bUseZLimiters]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200