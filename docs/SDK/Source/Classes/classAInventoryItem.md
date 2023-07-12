---
title: AInventoryItem
type: class
aliases: AInventoryItem
share: false

---

# AInventoryItem





Inherits from [ATBLActor](/docs/SDK/Source/Classes/classATBLActor.md), [IMatchStateListenerInterface](/docs/SDK/Source/Classes/classIMatchStateListenerInterface.md), AActor, [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[AInventoryItem]]**() |
| void | **[[AddBlacklistedPawn]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Player) |
| void | **[[AddIgnoreActors]]**(AActor * Initiator) |
| void | **[[AddToStackCount]]**(int32 Delta) |
| void | **[[ApplyDamage]]**(float InDamage) |
| void | **[[ApplyImpulseToGoreHead]]**(FVector Impulse) |
| void | **[[AttachSimulatedProjectileOnKill]]**(const FHitResult & HitResult) |
| void | **[[BounceOnProjectileHit]]**(const FHitResult & HitResult, [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * BlockingItem, float InBounceVelocityModifier) |
| bool | **[[CanUseItem]]**() |
| bool | **[[CannotAutoPickup]]**(APawn * Pawn) |
| void | **[[CheckStickPlayersToWall]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * KilledChar) |
| void | **[[ClientOnItemEquipped]]**(AActor * NewOwner) |
| void | **[[ClientOnItemUnequipped]]**() |
| void | **[[ClientToBeEquipped]]**() |
| void | **[[DestroyFakeClient]]**() |
| void | **[[DisableCollisionForFakeClient]]**() |
| bool | **[[DualWieldShouldUseBothWeaponsForAttack]]**(FName AttackName) |
| void | **[[EnableCollisionForFakeClient]]**([ATBLCharacterBase](/docs/SDK/Source/Classes/classATBLCharacterBase.md) * Character) |
| void | **[[EventUsePressed]]**(APawn * Pawn, [UInteractableComponent](/docs/SDK/Source/Classes/classUInteractableComponent.md) * InteractableComponent) |
| void | **[[FinishUnequippingOnAnimNotify]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character) |
| void | **[[GetAttachRagdollParams]]**([FAttachRagdollParams](/docs/SDK/Source/Classes/structFAttachRagdollParams.md) & AttachRagdollParams, [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character, const [FDeathDamageTakenEvent](/docs/SDK/Source/Classes/structFDeathDamageTakenEvent.md) & DamageEvent) |
| float | **[[GetBaseDamage]]**(FName AttackName) |
| [ATBLCharacterBase](/docs/SDK/Source/Classes/classATBLCharacterBase.md) * | **[[GetCarriedCharacter]]**() const |
| FString | **[[GetDamageSourceName]]**(FText & NameText) |
| float | **[[GetDamageSourcePenetration]]**() |
| [FInventoryItemDisplayInfo](/docs/SDK/Source/Classes/structFInventoryItemDisplayInfo.md) | **[[GetDisplayInfoForFaction]]**(EFaction Faction) const |
| [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * | **[[GetDualWieldOffhand]]**() |
| bool | **[[GetEquippableOnHorse]]**() |
| float | **[[GetHealth]]**() const |
| float | **[[GetHealthPercent]]**() const |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| EWeaponMaterial | **[[GetMaterialByWeaponAction]]**(bool IsAttacking, bool IsDefending, FName AttackName) |
| float | **[[GetMaxHealth]]**() const |
| UStaticMeshComponent * | **[[GetMesh]]**() const |
| [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * | **[[GetOwningPawn]]**() const |
| bool | **[[GetPendingHiddenInGame]]**() const |
| UPrimitiveComponent * | **[[GetPhysicsMesh]]**() const |
| [UProjectilePenetration](/docs/SDK/Source/Classes/classUProjectilePenetration.md) * | **[[GetProjectilePenetrationConfig]]**() |
| UPrimitiveComponent * | **[[GetShieldCollision]]**() |
| USkeletalMeshComponent * | **[[GetSkeletalMesh]]**() const |
| void | **[[GetSpecialAttackWindupSwitchOverride]]**(FString & SwitchState) |
| int32 | **[[GetStackCount]]**() |
| UShapeComponent * | **[[GetTeamProjectileCollision]]**() const |
| void | **[[InitDebugPreviousLocation]]**() |
| void | **[[InitializeGoreHead]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character, [FGoreHeadParams](/docs/SDK/Source/Classes/structFGoreHeadParams.md) Params, FVector Impulse) |
| void | **[[InitializeProjectileMovement]]**(AActor * Initiator, float InitialSpeed, bool bFakeClient) |
| void | **[[InitializeStackCountOnSpawn]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * CharacterOwner) |
| bool | **[[IsAbilityMultiAttack]]**(FName AttackName) |
| bool | **[[IsAddedToInventory]]**() |
| bool | **[[IsDualWieldOffhandEquipped]]**() |
| bool | **[[IsLowAmmo]]**() const |
| bool | **[[IsSimulatingPhysics]]**() const |
| bool | **[[IsTwoHandedWeapon]]**() |
| void | **[[LogShieldInfo]]**(const FString & LogText) |
| void | **[[NetMulticastFastSharedReplication]]**(const [FFastSharedProperties_InventoryItem](/docs/SDK/Source/Classes/structFFastSharedProperties__InventoryItem.md) & Properties) |
| void | **[[NetMulticastOnAddToInventoryItemPool]]**() |
| void | **[[OnAnimNotifyUseItem]]**([UTBLCharacterAnimInstance](/docs/SDK/Source/Classes/classUTBLCharacterAnimInstance.md) * AnimBP) |
| void | **[[OnAnimNotifyWeaponAttach]]**([UTBLCharacterAnimInstance](/docs/SDK/Source/Classes/classUTBLCharacterAnimInstance.md) * AnimBP) |
| void | **[[OnAnimNotifyWeaponDetach]]**([UTBLCharacterAnimInstance](/docs/SDK/Source/Classes/classUTBLCharacterAnimInstance.md) * AnimBP) |
| void | **[[OnAttackInterrupted]]**(int32 AttackID) |
| void | **[[OnCosmeticProjectilePenetration]]**(FHitResult Hit) |
| void | **[[OnDamaged]]**([FInventoryItemDamagedParams](/docs/SDK/Source/Classes/structFInventoryItemDamagedParams.md) Params) |
| void | **[[OnFakeClientProjectileHit]]**(const FHitResult & HitResult) |
| void | **[[OnInitialize]]**() |
| void | **[[OnMeleeSuccess]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * DamagedCharacter) |
| void | **[[OnMovementFinished]]**() |
| void | **[[OnMovementStarted]]**() |
| void | **[[OnPickupEnded]]**(AActor * Actor, FName CombatState, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) & EventAttackInfo, [UCombatState](/docs/SDK/Source/Classes/classUCombatState.md) * CombatStateBP) |
| void | **[[OnPlayActionEvent]]**(const [FSoundSwitchEntry](/docs/SDK/Source/Classes/structFSoundSwitchEntry.md) SoundSwitch) |
| void | **[[OnPlayerMeshChanged]]**(USkeletalMeshComponent * OldMesh, USkeletalMeshComponent * NewMesh) |
| void | **[[OnProjectileBounce]]**(FHitResult Hit, bool bParried) |
| void | **[[OnProjectileHit]]**(const FHitResult & HitResult) |
| void | **[[OnProjectileHitTarget]]**(FHitResult Hit) |
| void | **[[OnRep_HealthValue]]**() |
| void | **[[OnRep_IsOnFire]]**() |
| void | **[[OnRep_MountedItemParent]]**() |
| void | **[[OnRep_State]]**() |
| void | **[[OnRep_TornOffName]]**() |
| void | **[[OnUseItemEnded]]**(AActor * Actor, FName CombatState, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) & EventAttackInfo, [UCombatState](/docs/SDK/Source/Classes/classUCombatState.md) * CombatStateBP) |
| void | **[[OnWasParried]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * ParryingCharacter) |
| bool | **[[OverridePickupEvent]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character, bool bGiveWeapon, bool bIsAutoPickup) |
| void | **[[PerformFinishedMovementOverlap]]**() |
| int32 | **[[PlayActionEvent]]**(const [FSoundSwitchEntry](/docs/SDK/Source/Classes/structFSoundSwitchEntry.md) SoundSwitch) |
| void | **[[PlayEquipAnimation]]**() |
| void | **[[PlayImpactEvent]]**(const [FSoundSwitchEntry](/docs/SDK/Source/Classes/structFSoundSwitchEntry.md) SoundSwitch) |
| void | **[[ReloadThrownWeapon]]**() |
| void | **[[RemoveBlacklistedPawn]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Player) |
| void | **[[ResetItemToTransform]]**(FTransform Transform) |
| void | **[[ResetMaxStackCount]]**() |
| void | **[[SetAddedToInventory]]**(bool inAddedToInventory) |
| void | **[[SetDamagedState]]**(EInventoryItemDamagedState NewDamagedState) |
| void | **[[SetHealth]]**(float Health) |
| void | **[[SetInactive]]**() |
| void | **[[SetOffFire]]**() |
| void | **[[SetOnFire]]**() |
| void | **[[SetOverrideLifeSpan]]**(bool EnableOverride, float NewOverrideLifespan) |
| void | **[[SetPendingHiddenInGame]]**(bool NewBPendingHiddenInGame) |
| void | **[[SetRecentAttackReleaseWeaponActionSwitch]]**([FSoundSwitchEntry](/docs/SDK/Source/Classes/structFSoundSwitchEntry.md) Entry) |
| void | **[[SetStackCount]]**(int32 Count) |
| void | **[[SetupHapticsForPS5OnSpawningAttachment]]**(AController * InController) |
| bool | **[[ShouldAttachRagdoll]]**() |
| bool | **[[ShouldCustomizePlacedInWorldItem]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * OwningCharacter) |
| bool | **[[ShouldDropOnDowned]]**() |
| bool | **[[ShouldShowWIPInUI]]**() |
| void | **[[StartSimulatedProjectile]]**(int32 AttackID) |
| void | **[[UpdateVisualization]]**(float DeltaTime) |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[BroadcastAttachRagdoll]]**(FVector AttachLocation) |
| bool | **[[CanPickup]]**(APawn * Pawn) |
| USceneComponent * | **[[GetAttachRagdollComponent]]**() |
| void | **[[OnAttachedActorDestroyed]]**(AActor * DestroyedActor) |
| void | **[[OnAttachedActorKilled]]**(const [FDeathDamageTakenEvent](/docs/SDK/Source/Classes/structFDeathDamageTakenEvent.md) & Event) |
| void | **[[OnEquipCombatStateEnd]]**(AActor * Actor, FName CombatState, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) & EventAttackInfo, [UCombatState](/docs/SDK/Source/Classes/classUCombatState.md) * CombatStateBP) |
| void | **[[OnEquipComplete]]**() |
| void | **[[OnLocalPlayerStateReplicated]]**(APlayerState * PlayerState) |
| void | **[[OnReloadCombatStateEnd]]**(AActor * Actor, FName CombatState, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) & EventAttackInfo, [UCombatState](/docs/SDK/Source/Classes/classUCombatState.md) * CombatStateBP) |
| void | **[[OnRep_AddedToInventory]]**() |
| void | **[[OnRep_Drop]]**() |
| void | **[[OnRep_ProjectileHit]]**() |
| void | **[[OnRep_ResetToTransform]]**() |
| void | **[[OnRep_StackCount]]**() |
| void | **[[OnRep_UseFireAmmo]]**() |
| void | **[[OnUnequipCombatStateEnd]]**(AActor * Actor, FName CombatState, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) & EventAttackInfo, [UCombatState](/docs/SDK/Source/Classes/classUCombatState.md) * CombatStateBP) |
| void | **[[OnUnequipComplete]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * Character) |
| void | **[[SetUnequipped]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [FAIRanges](/docs/SDK/Source/Classes/structFAIRanges.md) | **[[AIRanges]]**  |
| [FWeaponAbilitySlots](/docs/SDK/Source/Classes/structFWeaponAbilitySlots.md) | **[[Abilities]]**  |
| float | **[[ActivationMaxDistanceOverride]]**  |
| float | **[[ActivationMinDistanceOverride]]**  |
| [FAimAssistTargetBoxData](/docs/SDK/Source/Classes/structFAimAssistTargetBoxData.md) | **[[AimAssistTargetBoxOverrides]]**  |
| float | **[[AimPenaltyModifier]]**  |
| TArray< [FAimAssistAttackData](/docs/SDK/Source/Classes/structFAimAssistAttackData.md) > | **[[AllowedAimAssistAttacks]]**  |
| [UWeaponTracersBlueprint](/docs/SDK/Source/Classes/classUWeaponTracersBlueprint.md) * | **[[AltTracerType]]**  |
| TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > | **[[AmmoItemClass]]**  |
| EAmmoStackType | **[[AmmoStackType]]**  |
| TArray< [FInventoryItemAnimation](/docs/SDK/Source/Classes/structFInventoryItemAnimation.md) > | **[[Animation]]**  |
| float | **[[AnimationSpeedModifier]]**  |
| [FArrowCamSettings](/docs/SDK/Source/Classes/structFArrowCamSettings.md) | **[[ArrowCamSettings]]**  |
| FName | **[[AttachAmmoSocket]]**  |
| TMap< EEquippedHand, [FInventoryAttachPointInfo](/docs/SDK/Source/Classes/structFInventoryAttachPointInfo.md) > | **[[AttachPoints]]**  |
| [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * | **[[AttachedAmmoItem]]**  |
| UAkComponent * | **[[AudioComponent]]**  |
| UAkAudioEvent * | **[[BattleCryOverrideAkEvent]]**  |
| [UMovementSequence](/docs/SDK/Source/Classes/classUMovementSequence.md) * | **[[Blocked]]**  |
| EBlockingCategory | **[[BlockingCategory]]**  |
| float | **[[BounceDamageParried]]**  |
| float | **[[BounceDamageWorld]]**  |
| float | **[[BounceVelocityModifier]]**  |
| TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > | **[[BrokenItemClass]]**  |
| uint8 | **[[CanBeDisarmed]]**  |
| TArray< EEquippedHand > | **[[CanBeEquipped]]**  |
| TArray< EInventoryItemSlot > | **[[CompatibleSlots]]**  |
| uint8 | **[[ConstructableLimit]]**  |
| TArray< [FInventoryItemAnimation](/docs/SDK/Source/Classes/structFInventoryItemAnimation.md) > | **[[CustomizationAnimation]]**  |
| EWeaponTag | **[[CustomizationWeaponTag]]**  |
| float | **[[Damage]]**  |
| float | **[[DamageModifier]]**  |
| UCurveVector * | **[[DamageScaleOnHorseback]]**  |
| [UDamageSource](/docs/SDK/Source/Classes/classUDamageSource.md) * | **[[DamageSource]]**  |
| UStaticMesh * | **[[DamagedMesh]]**  |
| float | **[[DamagedPercent]]**  |
| EInventoryItemDamagedState | **[[DamagedState]]**  |
| UStaticMesh * | **[[DestroyedMesh]]**  |
| uint8 | **[[DisabledInLoadout]]**  |
| [FInventoryItemDisplayInfo](/docs/SDK/Source/Classes/structFInventoryItemDisplayInfo.md) | **[[DisplayInfo]]**  |
| float | **[[DrawStrength]]**  |
| uint8 | **[[EquipOnPickup]]**  |
| float | **[[EquipTime]]**  |
| [FFakeClientBlendParams](/docs/SDK/Source/Classes/structFFakeClientBlendParams.md) | **[[FakeClientBlendParams]]**  |
| FName | **[[FakeClientSpawnPoint]]**  |
| TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > | **[[FireAmmoItemClass]]**  |
| [UDamageSource](/docs/SDK/Source/Classes/classUDamageSource.md) * | **[[FireDamage]]**  |
| USceneComponent * | **[[FirstPersonTransformRoot]]**  |
| float | **[[GlobalLifespan]]**  |
| TArray< [FWeaponGoreSlot](/docs/SDK/Source/Classes/structFWeaponGoreSlot.md) > | **[[GoreActions]]**  |
| float | **[[HealthValue]]**  |
| [FHorseAimingParams](/docs/SDK/Source/Classes/structFHorseAimingParams.md) | **[[HorseAimingParams]]**  |
| TArray< [FHorseAttackType](/docs/SDK/Source/Classes/structFHorseAttackType.md) > | **[[HorseAttackTypes]]**  |
| [UMovementSequence](/docs/SDK/Source/Classes/classUMovementSequence.md) * | **[[HorseLunge]]**  |
| TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > | **[[InheritAnimTimings]]**  |
| [FAimAssistFrictionData](/docs/SDK/Source/Classes/structFAimAssistFrictionData.md) | **[[InnerBoxFrictionData]]**  |
| [UInteractableComponent](/docs/SDK/Source/Classes/classUInteractableComponent.md) * | **[[Interactable]]**  |
| UAkAudioEvent * | **[[InventoryItemAKEvent_Action]]**  |
| UAkAudioEvent * | **[[InventoryItemAKEvent_Impact]]**  |
| UAkAudioEvent * | **[[InventoryItemAKEvent_ImpactThrown]]**  |
| [FReplicated_Int32](/docs/SDK/Source/Classes/structFReplicated__Int32.md) | **[[InvocationId]]**  |
| EItemSoundPolicy | **[[ItemSoundPolicy]]**  |
| EInventoryType | **[[ItemType]]**  |
| [UMovementSequence](/docs/SDK/Source/Classes/classUMovementSequence.md) * | **[[Knockback]]**  |
| float | **[[LowAmmoPercent]]**  |
| [UMovementSequence](/docs/SDK/Source/Classes/classUMovementSequence.md) * | **[[Lunge]]**  |
| [UMovementSequence](/docs/SDK/Source/Classes/classUMovementSequence.md) * | **[[LungeLeft]]**  |
| [UMovementSequence](/docs/SDK/Source/Classes/classUMovementSequence.md) * | **[[LungeRight]]**  |
| float | **[[MagnetismMoveSpeedModifierSelf]]**  |
| float | **[[MagnetismMoveSpeedModifierTarget]]**  |
| float | **[[MaxDrawPowerTime]]**  |
| uint8 | **[[MaxStackCount]]**  |
| EMeleeAttackCategory | **[[MeleeAttackCategory]]**  |
| float | **[[MinDrawPowerTime]]**  |
| float | **[[MinDrawStrength]]**  |
| TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > | **[[MountedItemClass]]**  |
| [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * | **[[MountedItemParent]]**  |
| [FDataTableRowSelection](/docs/SDK/Source/Classes/structFDataTableRowSelection.md) | **[[NoveltyScore]]**  |
| FOnAddedToInventoryChanged | **[[OnAddedToInventoryChanged]]**  |
| FOnAnimationSetChanged | **[[OnAnimationSetChanged]]**  |
| FOnBattleCryTriggered | **[[OnBattleCryTriggered]]**  |
| FOnDropped | **[[OnDropped]]**  |
| FOnFakeClientAttached | **[[OnFakeClientAttached]]**  |
| FOnOwnerChanged | **[[OnOwnerChanged]]**  |
| FOnDropped | **[[OnPreThrown]]**  |
| FOnProjectileHitEvent | **[[OnProjectileHitEvent]]**  |
| FOnSetAttached | **[[OnSetAttached]]**  |
| FOnSetOffFire | **[[OnSetOffFire]]**  |
| FOnSetOnFire | **[[OnSetOnFire]]**  |
| FOnSpawnFakeClient | **[[OnSpawnFakeClient]]**  |
| FOnDropped | **[[OnThrown]]**  |
| [FAimAssistFrictionData](/docs/SDK/Source/Classes/structFAimAssistFrictionData.md) | **[[OuterBoxFrictionData]]**  |
| TMap< EFaction, TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > > | **[[OverrideItemClassByTeam]]**  |
| float | **[[OverrideLifespan]]**  |
| TMap< TSoftClassPtr< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) >, uint8 > | **[[OverrideMaxStackCount]]**  |
| TMap< TSoftClassPtr< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) >, uint8 > | **[[OverrideStackCount]]**  |
| [FParryHitLocation](/docs/SDK/Source/Classes/structFParryHitLocation.md) | **[[ParryHitLocation]]**  |
| [UMovementSequence](/docs/SDK/Source/Classes/classUMovementSequence.md) * | **[[ParrySuccess]]**  |
| float | **[[PercentChanceToBreak]]**  |
| [FPickupItemSettings](/docs/SDK/Source/Classes/structFPickupItemSettings.md) | **[[PickupItemSettings]]**  |
| UAkAudioEvent * | **[[PickupItemSound]]**  |
| UAkAudioEvent * | **[[PickupManyItemSound]]**  |
| UBoxComponent * | **[[ProjectileCollision]]**  |
| UCurveFloat * | **[[ProjectileDistanceDamageScale]]**  |
| float | **[[ProjectileDrag]]**  |
| UCurveFloat * | **[[ProjectileDrawDamageScale]]**  |
| float | **[[ProjectileInitialRotation]]**  |
| [UTBLProjectileMovementComponent](/docs/SDK/Source/Classes/classUTBLProjectileMovementComponent.md) * | **[[ProjectileMovement]]**  |
| TWeakObjectPtr< AActor > | **[[ProjectileMovementInitiator]]**  |
| [UProjectilePenetration](/docs/SDK/Source/Classes/classUProjectilePenetration.md) * | **[[ProjectilePenetration]]**  |
| USceneComponent * | **[[ProjectileRoot]]**  |
| UCurveFloat * | **[[ProjectileRotationCurve]]**  |
| float | **[[ProjectileRotationRate]]**  |
| USceneComponent * | **[[ProjectileSmoothing]]**  |
| [FProjectileSounds](/docs/SDK/Source/Classes/structFProjectileSounds.md) | **[[ProjectileSounds]]**  |
| FVector | **[[ProjectileSpawnOffset]]**  |
| FName | **[[ProjectileSpawnPoint]]**  |
| TSubclassOf< [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) > | **[[QuiverItemClass]]**  |
| float | **[[RagdollImpulse]]**  |
| ERangedAttackCategory | **[[RangedAttackCategory]]**  |
| [UDamageSource](/docs/SDK/Source/Classes/classUDamageSource.md) * | **[[RangedDamageSource]]**  |
| [FSoundSwitchEntry](/docs/SDK/Source/Classes/structFSoundSwitchEntry.md) | **[[RecentAttackReleaseWeaponActionSwitch]]**  |
| FName | **[[ReloadCombatState]]**  |
| float | **[[ReloadTime]]**  |
| UCurveFloat * | **[[ReverseTurnLimitCurve]]**  |
| float | **[[ReverseTurnLimitStrength]]**  |
| float | **[[RiposteTime]]**  |
| float | **[[ShieldDamageModifier]]**  |
| [FShieldSettings](/docs/SDK/Source/Classes/structFShieldSettings.md) | **[[ShieldSettings]]**  |
| float | **[[SiegeDamage]]**  |
| ECharacterSignificanceLevel | **[[Significance]]**  |
| TSubclassOf< [USpecialItemAbility](/docs/SDK/Source/Classes/classUSpecialItemAbility.md) > | **[[SpecialItemAbility]]**  |
| ESpeedPenalty | **[[SpeedPenalty]]**  |
| uint8 | **[[StackCount]]**  |
| [FStaminaModifiers](/docs/SDK/Source/Classes/structFStaminaModifiers.md) | **[[StaminaModifiers]]**  |
| [FInventoryItemState](/docs/SDK/Source/Classes/structFInventoryItemState.md) | **[[State]]**  |
| UStaticMeshComponent * | **[[StaticMesh]]**  |
| UStaticMeshComponent * | **[[StaticMesh1PShadow]]**  |
| float | **[[StickPlayersToWallDistance]]**  |
| USceneComponent * | **[[StickPoint]]**  |
| float | **[[SwingWindDistance]]**  |
| FName | **[[ThirdPersonProjectileSpawnPointOverride]]**  |
| USceneComponent * | **[[ThirdPersonTransformRoot]]**  |
| [UAttackType](/docs/SDK/Source/Classes/classUAttackType.md) * | **[[ThrownAttackType]]**  |
| uint8 | **[[ThwackOnHit]]**  |
| [FReplicated_FName](/docs/SDK/Source/Classes/structFReplicated__FName.md) | **[[TornOffName]]**  |
| [UWeaponTracersBlueprint](/docs/SDK/Source/Classes/classUWeaponTracersBlueprint.md) * | **[[TracerType]]**  |
| UCurveFloat * | **[[TurnLimitCurve]]**  |
| UCurveFloat * | **[[TurnLimitScaleByDegreesTurned]]**  |
| float | **[[TurnLimitStrength]]**  |
| float | **[[UnequipTime]]**  |
| uint8 | **[[UseFirstAndThirdPersonTransformSetup]]**  |
| [FUseItemSettings](/docs/SDK/Source/Classes/structFUseItemSettings.md) | **[[UseItemSettings]]**  |
| bool | **[[UseProjectileSpawnOffsetAsProjectileOrigin]]**  |
| uint8 | **[[UseRangedCrossHair]]**  |
| int32 | **[[Version]]**  |
| UCurveFloat * | **[[VerticalTurnLimitCurve]]**  |
| float | **[[VerticalTurnLimitStrength]]**  |
| [UMovementSequence](/docs/SDK/Source/Classes/classUMovementSequence.md) * | **[[WasHitEarly]]**  |
| [FWeaponMaterialSoundConfig](/docs/SDK/Source/Classes/structFWeaponMaterialSoundConfig.md) | **[[WeaponActionMaterials]]**  |
| [UTBLParticleSystemComponent](/docs/SDK/Source/Classes/classUTBLParticleSystemComponent.md) * | **[[WeaponSwipeParticleComponent]]**  |
| [UTBLParticleSystemComponent](/docs/SDK/Source/Classes/classUTBLParticleSystemComponent.md) * | **[[WeaponThrowParticleComponent]]**  |
| EWeaponType | **[[WeaponType]]**  |
| [UMovementSequence](/docs/SDK/Source/Classes/classUMovementSequence.md) * | **[[WindupLunge]]**  |
| [FWorldHitAngleRange](/docs/SDK/Source/Classes/structFWorldHitAngleRange.md) | **[[WorldHitAngleRange]]**  |
| float | **[[WorldHitStartPercentage]]**  |
| float | **[[WorldHitStopPercentage]]**  |
| uint8 | **[[bAlignProjectilePitchToSurfaceOnStick]]**  |
| uint8 | **[[bAlwaysAutoPickup]]**  |
| bool | **[[bAlwaysEnableFriction]]**  |
| bool | **[[bAlwaysEnableInnerBoxForgiveness]]**  |
| bool | **[[bAlwaysFrictionInnerOnly]]**  |
| bool | **[[bAlwaysPrioritizeCloserTargets]]**  |
| bool | **[[bAlwaysScalingDistanceFrictionEnabled]]**  |
| uint8 | **[[bAutoPickupOwned]]**  |
| uint8 | **[[bAutomaticReload]]**  |
| uint8 | **[[bCanAttackWhileUnequipped]]**  |
| uint8 | **[[bCanBeLitOnFire]]**  |
| uint8 | **[[bCanFistsParry]]**  |
| uint8 | **[[bCanProjectileStick]]**  |
| uint8 | **[[bCanProjectileStickToShield]]**  |
| uint8 | **[[bCanStickPlayersToWall]]**  |
| uint8 | **[[bCanUseOffhandCarryable]]**  |
| uint8 | **[[bCannotEquipOnHorse]]**  |
| uint8 | **[[bClickToFire]]**  |
| uint8 | **[[bDisableJump]]**  |
| uint8 | **[[bDoNotAutoEquip]]**  |
| float | **[[bDropOffOnCharacterHitTime]]**  |
| uint8 | **[[bGenerateOverlapEventsWhenMovementFinished]]**  |
| uint8 | **[[bIsBreakable]]**  |
| uint8 | **[[bIsCarryableNPCItem]]**  |
| uint8 | **[[bIsCustomizationApplied]]**  |
| uint8 | **[[bIsDualWield]]**  |
| uint8 | **[[bIsFakeItem]]**  |
| uint8 | **[[bIsOnFire]]**  |
| uint8 | **[[bIsShield]]**  |
| uint8 | **[[bIsSlashCounteredByStab]]**  |
| uint8 | **[[bIsSpecialStabAnimation]]**  |
| uint8 | **[[bIsSpecialVerticalAnimation]]**  |
| uint8 | **[[bIsWIPItem]]**  |
| uint8 | **[[bLoaded]]**  |
| uint8 | **[[bNeedsUpdateVisualization]]**  |
| bool | **[[bOnlyTargetAllies]]**  |
| uint8 | **[[bPlaceOnGroundWhenSwapped]]**  |
| uint8 | **[[bPlayEquipAnimation]]**  |
| uint8 | **[[bPlayPickupAnimation]]**  |
| uint8 | **[[bProjectileAttachedViaReplication]]**  |
| uint8 | **[[bQuickThrowSpecial]]**  |
| bool | **[[bRotateProjectileCollision]]**  |
| uint8 | **[[bShouldScaleDrawStrength]]**  |
| uint8 | **[[bShouldSpecialIgnoreIsFacingTarget]]**  |
| uint8 | **[[bShouldStartOnFire]]**  |
| uint8 | **[[bTearOffOnMovementFinished]]**  |
| uint8 | **[[bTrackKillAchievement]]**  |
| uint8 | **[[bUseFireAmmo]]**  |
| bool | **[[bUseHorseAiming]]**  |
| uint8 | **[[bUseItemOnEquip]]**  |
| uint8 | **[[bUseOverrideLifespan]]**  |
| uint8 | **[[bUseRangedSignificance]]**  |
| bool | **[[bUseThirdPersonProjectileSpawnPointOverride]]**  |
| uint8 | **[[hasHealth]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| uint8 | **[[AddedToInventory]]**  |
| TArray< FName > | **[[AnimTimingProperties]]**  |
| FVector | **[[AttachRadollLocation]]**  |
| TSet< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * > | **[[BlacklistedPlayers]]**  |
| TWeakObjectPtr< [ATBLCharacterBase](/docs/SDK/Source/Classes/classATBLCharacterBase.md) > | **[[CarriedCharacter]]**  |
| [UWeaponTracers](/docs/SDK/Source/Classes/classUWeaponTracers.md) * | **[[CurrentWeaponTracers]]**  |
| FVector | **[[DebugPreviousLocation]]**  |
| [FInventoryAttachPointInfo](/docs/SDK/Source/Classes/structFInventoryAttachPointInfo.md) | **[[DefaultOffHandAttachPoint]]**  |
| [FInventoryAttachPointInfo](/docs/SDK/Source/Classes/structFInventoryAttachPointInfo.md) | **[[DefaultPrimaryAttachPoint]]**  |
| FTransform | **[[DefaultShieldCollisionRelativeTransform]]**  |
| TArray< [ATBLCharacterBase](/docs/SDK/Source/Classes/classATBLCharacterBase.md) * > | **[[FakeClientCollisionEnabled]]**  |
| [AInventoryItem](/docs/SDK/Source/Classes/classAInventoryItem.md) * | **[[FireAmmoItem]]**  |
| [UInventory](/docs/SDK/Source/Classes/classUInventory.md) * | **[[Inventory]]**  |
| int32 | **[[LastStackCount]]**  |
| [FInventoryAttachPointInfo](/docs/SDK/Source/Classes/structFInventoryAttachPointInfo.md) | **[[NoAttachPoint]]**  |
| FOnEquipped | **[[OnEquipped]]**  |
| FOnUseItem | **[[OnStartUseItem]]**  |
| FOnUseItem | **[[OnUseItem]]**  |
| float | **[[PrevAnimPercent]]**  |
| float | **[[PreviousAimPitch]]**  |
| FTransform | **[[PreviousArmBase]]**  |
| FTransform | **[[PreviousComponentTrs]]**  |
| [FReplicated_FReplicateDrop](/docs/SDK/Source/Classes/structFReplicated__FReplicateDrop.md) | **[[ReplicateDrop]]**  |
| [FReplicated_FProjectileHitParams](/docs/SDK/Source/Classes/structFReplicated__FProjectileHitParams.md) | **[[ReplicatedProjectileHit]]**  |
| [FReplicated_FResetToTransform](/docs/SDK/Source/Classes/structFReplicated__FResetToTransform.md) | **[[ResetToTransform]]**  |
| [FSimulatedProjectile](/docs/SDK/Source/Classes/structFSimulatedProjectile.md) | **[[SimulatedProjectile]]**  |
| FTransform | **[[SkeletalMeshTransform]]**  |
| EInventoryItemSlot | **[[Slot]]**  |
| uint8 | **[[bAttachAmmo]]**  |
| uint8 | **[[bFakeClientStickPoint]]**  |
| uint8 | **[[bIsAnimating]]**  |
| uint8 | **[[bMatchStateHidden]]**  |
| uint8 | **[[bPendingHiddenInGame]]**  |
| uint8 | **[[bPlacedInWorld]]**  |
| uint8 | **[[bShouldAttachRagdoll]]**  |
| uint8 | **[[bWasThrown]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:58 +0200