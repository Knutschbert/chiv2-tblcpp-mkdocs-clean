---
title: ABombard
type: class
aliases: ABombard
share: false

---

# ABombard





Inherits from [ASiegeEngine](/docs/SDK/Source/Classes/classASiegeEngine.md), [ILoadItemInterface](/docs/SDK/Source/Classes/classILoadItemInterface.md), [ATBLCharacterBase](/docs/SDK/Source/Classes/classATBLCharacterBase.md), [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md), [IDamagerInterface](/docs/SDK/Source/Classes/classIDamagerInterface.md), ACharacter, [ISignificanceInterface](/docs/SDK/Source/Classes/classISignificanceInterface.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[ABombard]]**() |
| void | **[[AddLogEntry]]**(const FString & LogEntry) |
| void | **[[BombardLoadItem]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Item, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Initiator) |
| void | **[[BroadcastStartFire]]**(const TArray< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * > & KnockbackCharacters) |
| void | **[[EventUsePressed]]**(APawn * InPawn, [UInteractableComponent](/docs/SDK/Source/Classes/classUInteractableComponent.md) * InInteractable) |
| EBombardState | **[[GetBombardState]]**() const |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| UPrimitiveComponent * | **[[GetLoadVolume]]**() |
| UPrimitiveComponent * | **[[GetReloadCollision]]**() |
| bool | **[[IsBroken]]**() const |
| bool | **[[IsInteractable]]**() const |
| bool | **[[IsPackaged]]**() const |
| bool | **[[IsPushable]]**() const |
| void | **[[K2_OnBombardStateChanged]]**(EBombardState State, EBombardState PreviousState) |
| void | **[[OnFire]]**() |
| void | **[[OnRep_BombardState]]**(EBombardState PreviousState) |
| void | **[[OnRep_FuseEndTime]]**() |
| void | **[[OnRep_LoadedAmmo]]**() |
| void | **[[OnRep_RotationPitch]]**() |
| void | **[[OnRep_RotationSpeed]]**() |
| void | **[[RemoveAttachedItem]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Item) |
| void | **[[SetBombardState]]**(EBombardState State) |
| void | **[[StartFire]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| bool | **[[CanLoad]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Item) |
| void | **[[ClientOnFire]]**() |
| bool | **[[IsBombardAmmo]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Item) const |
| void | **[[OnBombardFireAnimBegin]]**([UTBLBombardAnimInstance](/docs/SDK/Source/Classes/classUTBLBombardAnimInstance.md) * AnimInstance) |
| void | **[[OnBombardFireAnimComplete]]**() |
| void | **[[OnDamageTaken]]**(const [FDamageTakenEvent](/docs/SDK/Source/Classes/structFDamageTakenEvent.md) & Event) |
| void | **[[OnHealthChanged]]**(float Amount, AActor * Initiator) |
| void | **[[OnItemPickup]]**([AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * Item, bool IsAddedToInventory) |
| void | **[[OnKilled]]**(const [FDeathDamageTakenEvent](/docs/SDK/Source/Classes/structFDeathDamageTakenEvent.md) & Event) |
| void | **[[OnLoadVolumeBeginOverlap]]**(UPrimitiveComponent * OverlappedComponent, AActor * Other, UPrimitiveComponent * OtherComp, int32 OtherBodyIndex, bool bFromSweep, const FHitResult & OverlapInfo) |
| void | **[[OnLoadVolumeEndOverlap]]**(UPrimitiveComponent * OverlappedComponent, AActor * OtherActor, UPrimitiveComponent * OtherComp, int32 OtherBodyIndex) |
| void | **[[OnLoadedAmmoPorjectileMovementFinished]]**() |
| void | **[[OnPushableActivated]]**(bool IsActive) |
| void | **[[OnReloadCollision]]**(UPrimitiveComponent * OverlappedComponent, AActor * Other, UPrimitiveComponent * OtherComp, int32 OtherBodyIndex, bool bFromSweep, const FHitResult & OverlapInfo) |
| void | **[[ReadyToFire]]**() |
| void | **[[ServerPitchInput]]**(float Value) |
| void | **[[ServerStartFuse]]**() |
| void | **[[SetBroken]]**(bool bInBroken) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [UAbilitiesComponent](/docs/SDK/Source/Classes/classUAbilitiesComponent.md) * | **[[Abilities]]**  |
| TSubclassOf< UAnimInstance > | **[[AnimationBlueprint]]**  |
| TArray< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * > | **[[AttachedItems]]**  |
| float | **[[AutoLoadFacingAngle]]**  |
| float | **[[BaseTurnRate]]**  |
| [FProjectileSounds](/docs/SDK/Source/Classes/structFProjectileSounds.md) | **[[BombardProjectileSoundOverride]]**  |
| float | **[[BombardRecoilCharacterVelocity]]**  |
| [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * | **[[BombardSiegeWeapon]]**  |
| UAnimationAsset * | **[[BrokenAnimation]]**  |
| USkeletalMesh * | **[[BrokenMesh]]**  |
| UParticleSystem * | **[[BrokenParticle]]**  |
| [FSiegeEngineDamageSounds](/docs/SDK/Source/Classes/structFSiegeEngineDamageSounds.md) | **[[DamageSounds]]**  |
| USkeletalMesh * | **[[DamagedMesh]]**  |
| float | **[[DamagedThreshold]]**  |
| float | **[[DelayUntilPushbackKnockdown]]**  |
| UPhysicsAsset * | **[[DestroyedPhysAsset]]**  |
| float | **[[DrawStrength]]**  |
| TArray< UAkAudioEvent * > | **[[FiringSounds]]**  |
| float | **[[FuseDuration]]**  |
| float | **[[FuseEndTime]]**  |
| USkeletalMesh * | **[[HealthyMesh]]**  |
| uint8 | **[[IsBeingRotated]]**  |
| UAkAudioEvent * | **[[ItemLoadedSound]]**  |
| [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * | **[[LastLoadedAmmo]]**  |
| [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * | **[[LoadedAmmo]]**  |
| TWeakObjectPtr< [ATBLPlayerState](/docs/SDK/Source/Classes/classATBLPlayerState.md) > | **[[LoadedAmmoInstigator]]**  |
| FName | **[[LoadedAmmoSocketName]]**  |
| [UInteractableComponent](/docs/SDK/Source/Classes/classUInteractableComponent.md) * | **[[MountInteractable]]**  |
| UAkAudioEvent * | **[[MountSound]]**  |
| FVector | **[[MuzzleDestroyingBoxExtent]]**  |
| FOnBombardDamagedMeshApplied | **[[OnBombardDamagedMeshApplied]]**  |
| FOnBombardFireAction | **[[OnBombardFireAction]]**  |
| FOnBombardKilled | **[[OnBombardKilled]]**  |
| FBombardStateChanged | **[[OnBombardStateChanged]]**  |
| FOnFuseStarted | **[[OnFuseStarted]]**  |
| FOnBombardRepaired | **[[OnRepaired]]**  |
| float | **[[PitchLoopSoundFadeOutTime]]**  |
| float | **[[PitchMax]]**  |
| float | **[[PitchMin]]**  |
| UAkAudioEvent * | **[[PlayPitchLoopSound]]**  |
| UAkAudioEvent * | **[[PlayReloadLoopSound]]**  |
| UAkAudioEvent * | **[[PlayTurnLoopSound]]**  |
| UPhysicsAsset * | **[[PushablePhysAsset]]**  |
| [UPushingComponent](/docs/SDK/Source/Classes/classUPushingComponent.md) * | **[[PushingComponent]]**  |
| int32 | **[[PushingPriority]]**  |
| UAkAudioEvent * | **[[ReadyToFireSound]]**  |
| UBoxComponent * | **[[RecoilKnockback]]**  |
| [URepairableComponent](/docs/SDK/Source/Classes/classURepairableComponent.md) * | **[[Repairable]]**  |
| float | **[[RotationPitch]]**  |
| UPhysicsAsset * | **[[StationaryPhysAsset]]**  |
| [UStatsComponent](/docs/SDK/Source/Classes/classUStatsComponent.md) * | **[[Stats]]**  |
| UAkAudioEvent * | **[[StopPitchLoopSound]]**  |
| UAkAudioEvent * | **[[StopReloadLoopSound]]**  |
| UAkAudioEvent * | **[[StopTurnLoopSound]]**  |
| float | **[[TurnLimitStrength]]**  |
| TArray< TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > > | **[[WhitelistAmmoItemTypes]]**  |
| bool | **[[bDrawMuzzleExplosionExtent]]**  |
| bool | **[[bFocusHeld]]**  |
| bool | **[[bIsFiring]]**  |
| bool | **[[bKillPlayersInMuzzleExplosion]]**  |
| bool | **[[bReloadHeld]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| TWeakObjectPtr< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > | **[[BlockedAutoLoadCharacter]]**  |
| EBombardState | **[[BombardState]]**  |
| TWeakObjectPtr< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > | **[[FuseInitiatorDriver]]**  |
| int32 | **[[HorizLockId]]**  |
| FVector_NetQuantize10 | **[[InitialRotation]]**  |
| FRotator | **[[LastAimRotation]]**  |
| float | **[[LastPitchRate]]**  |
| [FProjectileSounds](/docs/SDK/Source/Classes/structFProjectileSounds.md) | **[[LoadedAmmoProjectileBackupSounds]]**  |
| TArray< USceneComponent * > | **[[LoadingComponentList]]**  |
| float | **[[MoveBackHeldTime]]**  |
| float | **[[MoveForwardHeldTime]]**  |
| TArray< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * > | **[[OverlappingCharacters]]**  |
| float | **[[PitchRate]]**  |
| int32 | **[[TurnRateId]]**  |
| int32 | **[[VertLockId]]**  |
| bool | **[[bIsBroken]]**  |
| bool | **[[bIsPlayingPitchSound]]**  |
| bool | **[[bMoveBackHeld]]**  |
| bool | **[[bMoveForwardHeld]]**  |
| bool | **[[bReplicatedIsBroken]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:58 +0200