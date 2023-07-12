---
title: UProjectileTargetMethod
type: class
aliases: UProjectileTargetMethod
share: false

---

# UProjectileTargetMethod





Inherits from [UCompositeTargetMethod](/docs/SDK/Source/Classes/classUCompositeTargetMethod.md), [UAbilityTargetMethod](/docs/SDK/Source/Classes/classUAbilityTargetMethod.md), [UTBLObject](/docs/SDK/Source/Classes/classUTBLObject.md), [UAssemblyObject](/docs/SDK/Source/Classes/classUAssemblyObject.md), UObject

Inherited by [UBombardTargetMethod](/docs/SDK/Source/Classes/classUBombardTargetMethod.md), [UCatapultTargetMethod](/docs/SDK/Source/Classes/classUCatapultTargetMethod.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[UProjectileTargetMethod]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[AddDelayedHit]]**(const FHitResult & Hit) |
| void | **[[HandleDelayedHits]]**() |
| void | **[[HandleDelayedHitsCosmetic]]**() |
| bool | **[[HandleParries]]**(FHitResult Hit, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * HitCharacter) |
| void | **[[HandlePassiveShieldHit]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Shield, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * HitCharacter, FHitResult Hit) |
| void | **[[OnBeginOverlap]]**(AActor * Other, UPrimitiveComponent * OtherComp, int32 OtherBodyIndex, bool bFromSweep, const FHitResult & OverlapInfo) |
| void | **[[OnBeginOverlapCosmetic]]**(AActor * Other, UPrimitiveComponent * OtherComp, int32 OtherBodyIndex, bool bFromSweep, const FHitResult & HitResult) |
| void | **[[OnHit]]**(AActor * OtherActor, UPrimitiveComponent * OtherComp, FVector NormalImpulse, const FHitResult & Hit) |
| void | **[[OnHitCosmetic]]**(AActor * OtherActor, UPrimitiveComponent * OtherComp, FVector NormalImpulse, const FHitResult & Hit) |
| void | **[[OnProjectileBeginPlay]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Item) |
| void | **[[OnProjectileDestroyed]]**(AActor * DestroyedActor) |
| void | **[[OnProjectileDestroyedCosmetic]]**(AActor * DestroyedActor) |
| void | **[[OnProjectileDisabled]]**() |
| void | **[[OnProjectileMovementFinished]]**() |
| void | **[[OnStop]]**(const FHitResult & Hit) |
| [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * | **[[SpawnProjectile]]**(FTransform SpawnTransform, bool bFakeClient, AActor * TargetProj, int32 InvocationId) |
| void | **[[UpdateFakeClientProjectile]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [UAbilityTargetMethod](/docs/SDK/Source/Classes/classUAbilityTargetMethod.md) * | **[[HitTargetMethod]]**  |
| FName | **[[ProjectileName]]**  |
| TArray< [UAction](/docs/SDK/Source/Classes/classUAction.md) * > | **[[ProjectileSpawnedActions]]**  |
| bool | **[[bHitDeactivatesInvocation]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| float | **[[AllowedClientSpawnLocationErrorSq]]**  |
| TArray< [UProjectileCollision](/docs/SDK/Source/Classes/classUProjectileCollision.md) * > | **[[CollisionHandlers]]**  |
| TWeakObjectPtr< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > | **[[CosmeticProjectile]]**  |
| TWeakObjectPtr< [UTBLProjectileMovementComponent](/docs/SDK/Source/Classes/classUTBLProjectileMovementComponent.md) > | **[[CosmeticProjectileMovement]]**  |
| TArray< FHitResult > | **[[DelayedCharacterHits]]**  |
| TArray< FHitResult > | **[[DelayedCharacterHitsCosmetic]]**  |
| TArray< FHitResult > | **[[DelayedNonCharacterHits]]**  |
| TArray< FHitResult > | **[[DelayedNonCharacterHitsCosmetic]]**  |
| FVector | **[[FakeClientInterpOffset]]**  |
| TWeakObjectPtr< [UTBLProjectileMovementComponent](/docs/SDK/Source/Classes/classUTBLProjectileMovementComponent.md) > | **[[FakeClientProjectile]]**  |
| TMap< TWeakObjectPtr< [UTBLProjectileMovementComponent](/docs/SDK/Source/Classes/classUTBLProjectileMovementComponent.md) >, TWeakObjectPtr< [UTBLProjectileMovementComponent](/docs/SDK/Source/Classes/classUTBLProjectileMovementComponent.md) > > | **[[FakeClientTargetMap]]**  |
| float | **[[FakeClientTotalTime]]**  |
| TWeakObjectPtr< USceneComponent > | **[[FakeClientUpdatedComponent]]**  |
| float | **[[LastFakeClientTime]]**  |
| TWeakObjectPtr< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > | **[[Projectile]]**  |
| TWeakObjectPtr< [UTBLProjectileMovementComponent](/docs/SDK/Source/Classes/classUTBLProjectileMovementComponent.md) > | **[[ProjectileMovement]]**  |
| bool | **[[bSpawnFakeProjectileOnServerRep]]**  |
| bool | **[[bWantsToFinish]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200