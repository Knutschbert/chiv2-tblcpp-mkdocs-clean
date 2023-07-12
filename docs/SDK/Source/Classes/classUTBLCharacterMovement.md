---
title: UTBLCharacterMovement
type: class
aliases: UTBLCharacterMovement
share: false

---

# UTBLCharacterMovement





Inherits from [UTBLCharacterMovementBaseComponent](/docs/SDK/Source/Classes/classUTBLCharacterMovementBaseComponent.md), UCharacterMovementComponent, [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[ApplyKnockback]]**([UMovementSequence](/docs/SDK/Source/Classes/classUMovementSequence.md) * Sequence, AActor * Initiator) |
| bool | **[[CanSprintAttack]]**() const |
| bool | **[[CanSprintShove]]**() const |
| void | **[[DisableCharacterCollision]]**() |
| void | **[[EnableCharacterCollision]]**() |
| void | **[[EndLadderMovement]]**() |
| void | **[[EndPhysSpawn]]**(bool bDisableRootMotion) |
| float | **[[GetChaseBonusPercent]]**() const |
| float | **[[GetDefaultMovementSpeed]]**() |
| TEnumAsByte< EMovementDirection > | **[[GetLastHorizontalInput]]**() const |
| TEnumAsByte< EMovementDirection > | **[[GetLastVerticalInput]]**() const |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| TEnumAsByte< EMovementDirection > | **[[GetMovementDirection]]**(bool bUseInputDirection, bool bUseLastNonZero) const |
| FVector | **[[GetMovementInputDirection]]**(bool bUseLastNonZero) const |
| FName | **[[GetMovementInputName]]**() const |
| float | **[[GetMovementSpeed]]**() const |
| FName | **[[GetMovementState]]**() const |
| [FSprintState](/docs/SDK/Source/Classes/structFSprintState.md) | **[[GetSprintState]]**() |
| float | **[[GetSprintTime]]**() |
| void | **[[HandleDelaySpawnAnimation]]**() |
| bool | **[[IsCrouchKeyHeld]]**() |
| bool | **[[IsSprintDecelerating]]**() const |
| bool | **[[IsSprinting]]**() const |
| void | **[[LadderDismountPressed]]**() |
| void | **[[LadderDismountReleased]]**() |
| float | **[[MoveDirectionToAngle]]**(TEnumAsByte< EMovementDirection > Direction) const |
| FVector | **[[MoveDirectionToVector]]**(TEnumAsByte< EMovementDirection > Direction) const |
| void | **[[MoveIgnoreActorAdd]]**(AActor * ActorToIgnore) |
| void | **[[MoveIgnoreActorRemove]]**(AActor * ActorToIgnore) |
| void | **[[PlaySpawnAnimation]]**(FName Animation) |
| void | **[[PlaySpawnAnimation_Internal]]**(FName Animation) |
| void | **[[ServerLadderDismountPressed]]**() |
| void | **[[ServerPlaySpawnAnimation]]**(FName Animation, float ActorYaw, float ClientTimeStamp) |
| void | **[[SetAltAttackWithMovement]]**(bool bEnable) |
| void | **[[SetAutoSprint]]**(bool bEnable) |
| void | **[[SetAutoSprintKey]]**(bool bSprint) |
| void | **[[SetAutorunElapsedTime]]**(float ElapsedTime) |
| void | **[[SetSprintKey]]**(bool bSprint) |
| void | **[[SetSprintLocked]]**(bool bSprintLock) |
| void | **[[SetWalkKey]]**(bool bWalk) |
| void | **[[SprintDecelerateToSprint]]**(float Speed) |
| void | **[[SprintKeyPressed]]**() |
| void | **[[SprintKeyReleased]]**() |
| void | **[[StartAutoSprint]]**() |
| void | **[[StartCrouch]]**() |
| void | **[[StartDash]]**() |
| void | **[[StartJump]]**() |
| void | **[[StopCrouch]]**() |
| | **[[UTBLCharacterMovement]]**() |
| void | **[[WalkKeyPressed]]**() |
| void | **[[WalkKeyReleased]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[BroadcastDownToUpLadderAnimation]]**() |
| void | **[[BroadcastIgnoreActorWhenMoving]]**(AActor * ActorToIgnore, bool bShouldIgnore) |
| void | **[[BroadcastPlayLadderAnimation]]**(FName Animation) |
| void | **[[BroadcastSetCharacterCollision]]**(bool bEnabled) |
| void | **[[BroadcastStartVault]]**([AVaultMarker](/docs/SDK/Source/Classes/classAVaultMarker.md) * VaultMarker) |
| bool | **[[CanSprint]]**(bool bStartSprint) const |
| void | **[[ClientForceLadderMovement]]**(bool bDirectionUp) |
| void | **[[ClientMountLadderFailed]]**() |
| void | **[[DownedSprintFinished]]**() |
| void | **[[DownedSprintStart]]**() |
| void | **[[DownedSprintTick]]**(float DeltaSeconds) |
| void | **[[ForceMaxSprint]]**() |
| void | **[[LimitSprintTurnRate]]**(float DeltaTime) |
| void | **[[OnActorHit]]**(AActor * SelfActor, AActor * OtherActor, FVector NormalImpulse, const FHitResult & Hit) |
| void | **[[OnCombatStateChanged]]**(AActor * Actor, FName PreviousState, FName NewState, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) & EventAttackInfo, [UCombatState](/docs/SDK/Source/Classes/classUCombatState.md) * CombatState) |
| void | **[[OnDismount]]**(AActor * AttachParent, EDismountType DismountType) |
| void | **[[OnEquippedItemsChanged]]**() |
| void | **[[OnLadderAnimationEnded]]**() |
| void | **[[OnRep_CharacterMovementState]]**() |
| void | **[[OnRep_RepCurrentSpawnBoost]]**() |
| void | **[[OnRep_ReplicatedSprintTurn]]**() |
| void | **[[ResumeSprintCombatState]]**() |
| void | **[[ServerEndLadderMovement]]**([FEndLadderMovement](/docs/SDK/Source/Classes/structFEndLadderMovement.md) Params) |
| void | **[[ServerMountLadder]]**(float ClientTimeStamp) |
| void | **[[ServerPlayLadderAnimation]]**([FPlayLadderAnimation](/docs/SDK/Source/Classes/structFPlayLadderAnimation.md) Params) |
| void | **[[ServerSetDowned]]**(bool bDowned, float ClientTimeStamp) |
| void | **[[ServerSetMoveBackward]]**(bool bPressed) |
| void | **[[ServerSetMoveLeft]]**(bool bPressed) |
| void | **[[ServerSetMoveRight]]**(bool bPressed) |
| void | **[[ServerStartSpawnBonus]]**(const [FStartSpawnBonus](/docs/SDK/Source/Classes/structFStartSpawnBonus.md) & Params) |
| void | **[[SetDownedAutonomous]]**() |
| void | **[[SetDownedTurnRate]]**(bool bDowned) |
| void | **[[SprintDecelerate]]**() |
| void | **[[SprintDecelerateTick]]**(float DeltaSeconds) |
| void | **[[SprintFinished]]**() |
| void | **[[SprintStart]]**() |
| void | **[[SprintStartTick]]**(float DeltaSeconds) |
| void | **[[SprintTick]]**(float DeltaSeconds) |
| void | **[[SprintTurnDecelerate]]**() |
| void | **[[SprintTurnTick]]**(float DeltaSeconds) |
| void | **[[UpdateSprint]]**(float DeltaTime) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| float | **[[AutoSprintDelay]]**  |
| float | **[[BackSpeedModifier]]**  |
| FVector2D | **[[BackStrafeSpeedModifier]]**  |
| [FChaseMechanicParams](/docs/SDK/Source/Classes/structFChaseMechanicParams.md) | **[[ChaseMechanicParams]]**  |
| float | **[[CurrentAimPenalty]]**  |
| float | **[[CurrentRangedInaccuracy]]**  |
| FName | **[[DelayPlaySpawnAnimation]]**  |
| float | **[[DisableSlideMaxAngle]]**  |
| [FDisableSprintAttackOnQuickTurn](/docs/SDK/Source/Classes/structFDisableSprintAttackOnQuickTurn.md) | **[[DisableSprintAttackOnQuickTurn]]**  |
| float | **[[DownedCapsuleHalfHeight]]**  |
| float | **[[DownedCapsuleRadius]]**  |
| float | **[[DownedTurnLimit]]**  |
| float | **[[ForwardSpeedModifier]]**  |
| FVector2D | **[[ForwardStrafeSpeedModifier]]**  |
| float | **[[GamepadUsePressedTime]]**  |
| [FReplicated_Bool](/docs/SDK/Source/Classes/structFReplicated__Bool.md) | **[[InventoryCanJump]]**  |
| [FReplicated_Float](/docs/SDK/Source/Classes/structFReplicated__Float.md) | **[[InventorySpeedPenalty]]**  |
| [FLandingSlowDownParams](/docs/SDK/Source/Classes/structFLandingSlowDownParams.md) | **[[LandingSlowDownParams]]**  |
| float | **[[MinimumCrouchTime]]**  |
| float | **[[MoveBackwardHeldTime]]**  |
| float | **[[MoveForwardHeldTime]]**  |
| float | **[[MoveLeftHeldTime]]**  |
| float | **[[MoveRightHeldTime]]**  |
| FOnCrouch | **[[OnCrouch]]**  |
| FOnDash | **[[OnDash]]**  |
| FCharJumpedSignature | **[[OnJump]]**  |
| FCharJumpedSignature | **[[OnJumpPressed]]**  |
| FCharLandedSignature | **[[OnLanded]]**  |
| FOnMovementInput | **[[OnMovementInput]]**  |
| FMovementStateChangedSignature | **[[OnMovementStateChanged]]**  |
| FOnMovementStateUpdate | **[[OnMovementStateUpdate]]**  |
| FMovementSyncSignature | **[[OnMovementSync]]**  |
| FPlayAnimation | **[[OnPlayLadderAnimation]]**  |
| FPlayAnimation | **[[OnPlaySpawnAnimation]]**  |
| FPostLockMovement | **[[OnPostLockMovement]]**  |
| FReverseAnimation | **[[OnReverseLadderAnimation]]**  |
| FCharSprintStateSignature | **[[OnSprintState]]**  |
| FSprintStopSignature | **[[OnSprintStop]]**  |
| FOnSprintTurn | **[[OnSprintTurn]]**  |
| FStartedFallingSignature | **[[OnStartedFalling]]**  |
| FOnVaultSignature | **[[OnVault]]**  |
| [FReplicated_Float](/docs/SDK/Source/Classes/structFReplicated__Float.md) | **[[PerksSpeedBonus]]**  |
| FVector | **[[PreMoveVelocity]]**  |
| [FSpawnState](/docs/SDK/Source/Classes/structFSpawnState.md) | **[[SpawnState]]**  |
| float | **[[SprintForwardAcceleration]]**  |
| int32 | **[[SprintHorizLockTurnId]]**  |
| float | **[[SprintStrafeAcceleration]]**  |
| FVector2D | **[[SprintStrafeSpeedModifier]]**  |
| [FSprintTurnParams](/docs/SDK/Source/Classes/structFSprintTurnParams.md) | **[[SprintTurnParams]]**  |
| int32 | **[[SprintVerticalLockTurnId]]**  |
| float | **[[StrafeSpeedModifier]]**  |
| float | **[[ViewPitchInterpSpeed]]**  |
| float | **[[ViewPitchMaxCrouching]]**  |
| float | **[[ViewPitchMaxSpinningSpecial]]**  |
| float | **[[ViewPitchMaxStanding]]**  |
| float | **[[ViewPitchMinCrouching]]**  |
| float | **[[ViewPitchMinSpinningSpecial]]**  |
| float | **[[ViewPitchMinStanding]]**  |
| float | **[[ViewPitchSpinningSpecialInterpSpeed]]**  |
| bool | **[[bAltAttackWithMovement]]**  |
| bool | **[[bAutoSprint]]**  |
| bool | **[[bDisableJump]]**  |
| bool | **[[bForceWalk]]**  |
| bool | **[[bGamepadSprint]]**  |
| uint8 | **[[bIsMovementLocked]]**  |
| bool | **[[bMoveBackwardHeld]]**  |
| bool | **[[bMoveForwardHeld]]**  |
| bool | **[[bMoveLeftHeld]]**  |
| bool | **[[bMoveRightHeld]]**  |
| bool | **[[bPlayingSpawnAnimation]]**  |
| bool | **[[bSprintLocked]]**  |
| bool | **[[bWantsToAutoSprint]]**  |
| bool | **[[bWantsToSprint]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| TArray< [FAimPenalty](/docs/SDK/Source/Classes/structFAimPenalty.md) > | **[[ActiveAimPenalties]]**  |
| TArray< [FScaleDirectionParams](/docs/SDK/Source/Classes/structFScaleDirectionParams.md) > | **[[ActiveScaleDirection]]**  |
| [FReplicated_FName](/docs/SDK/Source/Classes/structFReplicated__FName.md) | **[[CharacterMovementState]]**  |
| [FReplicated_Float](/docs/SDK/Source/Classes/structFReplicated__Float.md) | **[[ChaseBonus]]**  |
| float | **[[ChaseTime]]**  |
| float | **[[CrouchStartTime]]**  |
| FFindFloorResult | **[[CurrentFollowGround]]**  |
| float | **[[DashCooldown]]**  |
| float | **[[DefaultMovementSpeed]]**  |
| [FDismountBlendParams](/docs/SDK/Source/Classes/structFDismountBlendParams.md) | **[[DismountBlendParams]]**  |
| float | **[[DownedMovementSpeed]]**  |
| float | **[[DownedSprintSpeed]]**  |
| int32 | **[[DownedTurnRateId]]**  |
| float | **[[FallingStartTime]]**  |
| float | **[[JumpCooldown]]**  |
| float | **[[JumpFromDashCooldown]]**  |
| [FLadderRootMotionBlend](/docs/SDK/Source/Classes/structFLadderRootMotionBlend.md) | **[[LadderRootMotionBlend]]**  |
| [FLadderRotationBlend](/docs/SDK/Source/Classes/structFLadderRotationBlend.md) | **[[LadderRotationBlend]]**  |
| [FLadderState](/docs/SDK/Source/Classes/structFLadderState.md) | **[[LadderState]]**  |
| float | **[[LastDashTime]]**  |
| double | **[[LastFindFloorTime]]**  |
| FVector | **[[LastHitDirection]]**  |
| [FReplicated_EMovementDirection](/docs/SDK/Source/Classes/structFReplicated__EMovementDirection.md) | **[[LastHorizontalInput]]**  |
| float | **[[LastLandedTime]]**  |
| FVector | **[[LastNonZeroAcceleration]]**  |
| FVector | **[[LastNonZeroVelocity]]**  |
| float | **[[LastTickSprintSpeed]]**  |
| float | **[[LastTurnTime]]**  |
| [FReplicated_EMovementDirection](/docs/SDK/Source/Classes/structFReplicated__EMovementDirection.md) | **[[LastVerticalInput]]**  |
| int32 | **[[MovementBlockId]]**  |
| [UMovementModifierComponent](/docs/SDK/Source/Classes/classUMovementModifierComponent.md) * | **[[MovementModifiers]]**  |
| float | **[[MovementSpeed]]**  |
| [FReplicated_Float](/docs/SDK/Source/Classes/structFReplicated__Float.md) | **[[RepCurrentSpawnBoost]]**  |
| [FReplicated_FReplicatedSprintTurn](/docs/SDK/Source/Classes/structFReplicated__FReplicatedSprintTurn.md) | **[[ReplicatedSprintTurn]]**  |
| int32 | **[[ScaleDirectionalMovementId]]**  |
| [FSpawnBoost](/docs/SDK/Source/Classes/structFSpawnBoost.md) | **[[SpawnBoost]]**  |
| float | **[[SprintBaseSpeed]]**  |
| float | **[[SprintDeceleration]]**  |
| float | **[[SprintMaxSpeed]]**  |
| float | **[[SprintStartMinTime]]**  |
| float | **[[SprintStartTime]]**  |
| [FSprintState](/docs/SDK/Source/Classes/structFSprintState.md) | **[[SprintState]]**  |
| float | **[[SprintTime]]**  |
| [UStatsComponent](/docs/SDK/Source/Classes/classUStatsComponent.md) * | **[[Stats]]**  |
| float | **[[StrafeAccelerationModifier]]**  |
| FVector | **[[TeleportLocation]]**  |
| FRotator | **[[TeleportRotation]]**  |
| float | **[[TeleportTime]]**  |
| int32 | **[[UpdateSpawnBonusHandle]]**  |
| bool | **[[bCharacterCollisionEnabled]]**  |
| bool | **[[bForceMaxSprint]]**  |
| bool | **[[bIsAutorunSprinting]]**  |
| bool | **[[bIsCrouchHeld]]**  |
| bool | **[[bIsCrouchKeyHeld]]**  |
| uint8 | **[[bIsDowned]]**  |
| uint8 | **[[bIsPossessed]]**  |
| [FReplicated_Bool](/docs/SDK/Source/Classes/structFReplicated__Bool.md) | **[[bIsSprinting]]**  |
| float | **[[bMovementBlockEndOnLanding]]**  |
| bool | **[[bTeleport]]**  |

-------------------------------

Updated on 2023-07-04 at 02:31:00 +0200