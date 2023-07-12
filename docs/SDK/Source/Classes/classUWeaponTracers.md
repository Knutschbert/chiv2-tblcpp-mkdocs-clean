---
title: UWeaponTracers
type: class
aliases: UWeaponTracers
share: false

---

# UWeaponTracers





Inherits from [UAssemblyInstance](/docs/SDK/Source/Classes/classUAssemblyInstance.md), UObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[ActivateAttackTracers]]**() |
| void | **[[DoWeaponTracers]]**() |
| void | **[[EndWeaponTracers]]**() |
| void | **[[Initialize]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Weapon, const [UWeaponTracersBlueprint](/docs/SDK/Source/Classes/classUWeaponTracersBlueprint.md) * SourceObj) |
| bool | **[[IsValid]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Weapon) const |
| void | **[[StartWeaponTracers]]**() |
| | **[[UWeaponTracers]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[CalcTracerPoints]]**() |
| bool | **[[CheckTargetVisibility]]**(AActor * Target) |
| void | **[[CopyPreviousFrame]]**() |
| bool | **[[DidEarlyHit]]**(FHitResult & Hit, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) *& OutCharacter) const |
| bool | **[[DidHeadShot]]**(FHitResult & Hit) const |
| bool | **[[DidHitActor]]**(AActor * HitActor) const |
| bool | **[[DidHitActorWithStats]]**(FHitResult & Hit, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) *& OutCharacter) const |
| bool | **[[DidHitCharacter]]**(FHitResult & Hit, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) *& OutCharacter) const |
| bool | **[[DidHitDeadCharacter]]**(FHitResult & Hit, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) *& OutCharacter) const |
| bool | **[[DidHitDeadHorse]]**(FHitResult & Hit, [AHorse](/docs/SDK/Source/Classes/classAHorse.md) *& OutHorse) const |
| bool | **[[DidHitInventoryItem]]**(FHitResult & Hit, [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) *& OutInventoryItem) const |
| bool | **[[DidHitParryBox]]**(FHitResult & Hit, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) *& OutCharacter) const |
| bool | **[[DidHitWorld]]**(FHitResult & Hit, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) *& OutCharacter) const |
| bool | **[[DidReleaseClash]]**(FHitResult & Hit, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) *& OutCharacter) const |
| void | **[[DoTracerCollisionCheck]]**() |
| void | **[[DrawDebugParryHit]]**(FVector Loc) |
| void | **[[HandleEarlyHitCharacter]]**(FHitResult & Hit, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * HitChar) |
| void | **[[HandleHitActorWithStats]]**(FHitResult & Hit) |
| bool | **[[HandleHitCharacter]]**(FHitResult & Hit, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * HitChar) |
| void | **[[HandleHitDeadCharacter]]**(FHitResult & Hit, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * HitChar) |
| void | **[[HandleHitDeadHorse]]**(FHitResult & Hit, [AHorse](/docs/SDK/Source/Classes/classAHorse.md) * HitHorse) |
| void | **[[HandleHitInventoryItem]]**(FHitResult & Hit, [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * HitInventoryItem) |
| bool | **[[HandleHitParry]]**(FHitResult & Hit, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * HitChar) |
| void | **[[HandleHitWorld]]**(FHitResult & Hit, [UTracerShape](/docs/SDK/Source/Classes/classUTracerShape.md) * TracerShape) |
| void | **[[HandleReleaseClash]]**(FHitResult & Hit, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * HitChar) |
| bool | **[[IgnoreHitActorWithStats]]**(FHitResult & Hit) |
| void | **[[SaveHitActor]]**(AActor * HitActor) |
| void | **[[SetTracerFrame]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| TArray< [UTracerType](/docs/SDK/Source/Classes/classUTracerType.md) * > | **[[TracerList]]**  |
| bool | **[[bHasTracerCache]]**  |
| bool | **[[bOnlyParryTracers]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| [UTracerShape](/docs/SDK/Source/Classes/classUTracerShape.md) * | **[[CurrentTracerShape]]**  |
| [UTracerType](/docs/SDK/Source/Classes/classUTracerType.md) * | **[[CurrentTracers]]**  |
| TArray< AActor * > | **[[HitActorsThisFrame]]**  |
| [FTracerCacheParams](/docs/SDK/Source/Classes/structFTracerCacheParams.md) | **[[Params]]**  |
| TArray< AActor * > | **[[ParryActors]]**  |
| int32 | **[[TracerFrame]]**  |
| bool | **[[bTracerActive]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:01 +0200