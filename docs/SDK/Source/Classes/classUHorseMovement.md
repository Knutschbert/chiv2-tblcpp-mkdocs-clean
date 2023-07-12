---
title: UHorseMovement
type: class
aliases: UHorseMovement
share: false

---

# UHorseMovement





Inherits from [USiegeEngineMovement](/docs/SDK/Source/Classes/classUSiegeEngineMovement.md), [UTBLCharacterMovementBaseComponent](/docs/SDK/Source/Classes/classUTBLCharacterMovementBaseComponent.md), UCharacterMovementComponent, [IReplicatedSubobjectInterface](/docs/SDK/Source/Classes/classIReplicatedSubobjectInterface.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| bool | **[[CheckHorseCollisionFromIdle]]**(float Direction) |
| FName | **[[ClampMovementState]]**(FName State) |
| void | **[[ClientPerformBump]]**(float Direction, float TurnAngle, float Scale, bool bRearImpact, bool bSideImpact, [AHorse](/docs/SDK/Source/Classes/classAHorse.md) * InitiatorHorse) |
| void | **[[DrawDebugHorseMovePath]]**(float DeltaTime) |
| bool | **[[GetBoostMode]]**() |
| bool | **[[GetControlMode]]**() |
| float | **[[GetCurrentForwardSpeed]]**() |
| void | **[[GetInputDirection]]**(EHorseMovementInput & Direction, float & HeldTime) |
| void | **[[GetInputForward]]**(float & InputForward, float & HeldTime) |
| void | **[[GetInputStrafe]]**(float & InputStrafe, float & HeldTime) |
| void | **[[GetInputTurn]]**(float & InputTurn, float & HeldTime) |
| float | **[[GetInstantKickSpeed]]**() |
| bool | **[[GetInvertedBackwardsStrafe]]**() |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| float | **[[GetMaxKickSpeed]]**() |
| float | **[[GetMaxSpeedInState]]**(FName State) |
| float | **[[GetMinSpeedInState]]**(FName State) |
| FName | **[[GetMovementStateFromSpeed]]**(float Speed) |
| float | **[[GetSettleSpeedInState]]**(FName State) |
| float | **[[GetSpeedInState]]**(FName State, float Percent) |
| void | **[[ImpactBumpOff]]**() |
| void | **[[ImpactMaxSpeed]]**(float MaxSpeed, float Time) |
| void | **[[ImpactSlowdown]]**(float Delta, float Time) |
| void | **[[ImpactTurn]]**(float Delta, float Time) |
| bool | **[[IsMovementStateEqual]]**(FName State) |
| bool | **[[IsMovementStateGreaterThan]]**(FName State) |
| bool | **[[IsMovementStateLessThanEqual]]**(FName State) |
| bool | **[[IsStrafing]]**() |
| bool | **[[IsValidMovementState]]**(FName State) |
| void | **[[ModifyAccelerationScale]]**(float Target, float InterpSpeed) |
| void | **[[ModifyTargetSpeed]]**(float Target) |
| void | **[[ModifyTurnRateScale]]**(float Target, float InterpSpeed) |
| void | **[[OnRep_CurrentForwardSpeed]]**() |
| void | **[[OnRep_CurrentTurnRate]]**() |
| void | **[[OnRep_CurrentTurnRateAccel]]**() |
| void | **[[OnRep_IsAccelerating]]**() |
| void | **[[OnRep_IsDecelerating]]**() |
| void | **[[OnRep_TargetSpeed]]**() |
| void | **[[ServerHorseToHorseBump]]**([FHorseToHorseBump](/docs/SDK/Source/Classes/structFHorseToHorseBump.md) Params) |
| void | **[[ServerHorseToWorldBump]]**([FHorseToWorldBump](/docs/SDK/Source/Classes/structFHorseToWorldBump.md) Params) |
| void | **[[StartDash]]**() |
| void | **[[TurnTowardsCamera]]**(float TurnRate, float TurnRateWithInput) |
| | **[[UHorseMovement]]**() |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[BroadcastBump]]**(AActor * Actor, float TurnAngle, float BumpVelocity, bool bDirection, bool bRearImpact) |
| void | **[[BroadcastHorseToCharacterImpact]]**([ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) * TargetCharacter, EHorseImpactLocation HorseImpactLocation, EHorseToCharacterImpactType ImpactType, FName ImpactCombatState, float ImpactSpeed) |
| void | **[[BroadcastHorseToHorseImpact]]**([AHorse](/docs/SDK/Source/Classes/classAHorse.md) * TargetHorse, EHorseImpactLocation HorseImpactLocation, EHorseToHorseImpactType ImpactType, FName ImpactCombatState, float ImpactSpeed) |
| void | **[[BroadcastHorseToWorldImpact]]**(FHitResult Hit, EHorseImpactLocation HorseImpactLocation, EHorseToWorldImpactType ImpactType, FName ImpactCombatState, float ImpactSpeed) |
| void | **[[ClientImpactMaxSpeed]]**(float MaxSpeed, float Time) |
| void | **[[ClientImpactSlowdown]]**(float Delta, float Time) |
| void | **[[ClientImpactTurn]]**(float Delta, float Time) |
| void | **[[OnCombatStateChanged]]**(AActor * Actor, FName PreviousState, FName NewState, const [FAttackInfo](/docs/SDK/Source/Classes/structFAttackInfo.md) & EventAttackInfo, [UCombatState](/docs/SDK/Source/Classes/classUCombatState.md) * CombatState) |
| void | **[[OnPushingOverlap]]**(TArray< [ATBLCharacterBase](/docs/SDK/Source/Classes/classATBLCharacterBase.md) * > Overlaps) |
| void | **[[ServerSetLeanDirection]]**(FName Direction) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [FHorseMovementScale](/docs/SDK/Source/Classes/structFHorseMovementScale.md) | **[[AccelerationScale]]**  |
| float | **[[CruisingSpeed]]**  |
| float | **[[CurrentForwardAccel]]**  |
| float | **[[CurrentForwardSpeed]]**  |
| float | **[[CurrentMovementModifier]]**  |
| [FHorseMovementData](/docs/SDK/Source/Classes/structFHorseMovementData.md) | **[[CurrentMovementState]]**  |
| float | **[[CurrentStrafeAccel]]**  |
| float | **[[CurrentStrafeDistance]]**  |
| float | **[[CurrentStrafeSpeed]]**  |
| float | **[[CurrentTurnRate]]**  |
| float | **[[CurrentTurnRateAccel]]**  |
| float | **[[ForceRunTime]]**  |
| float | **[[HorseMovementDirectionTimeMs]]**  |
| float | **[[HorseMovementInfoTimeMs]]**  |
| float | **[[ModifiedForwardSpeed]]**  |
| FHorseBreaking | **[[OnBreaking]]**  |
| FHorseLandedSignature | **[[OnLanded]]**  |
| FHorseWantsToGallop | **[[OnWantsToGallop]]**  |
| float | **[[PendingTargetSpeed]]**  |
| float | **[[PreviousSpeed]]**  |
| [FReplicated_Float](/docs/SDK/Source/Classes/structFReplicated__Float.md) | **[[ReplicatedCurrentForwardSpeed]]**  |
| [FReplicated_Float](/docs/SDK/Source/Classes/structFReplicated__Float.md) | **[[ReplicatedCurrentTurnRate]]**  |
| [FReplicated_Float](/docs/SDK/Source/Classes/structFReplicated__Float.md) | **[[ReplicatedCurrentTurnRateAccel]]**  |
| FVector_NetQuantizeNormal | **[[ReplicatedFloorNormal]]**  |
| [FReplicated_Float](/docs/SDK/Source/Classes/structFReplicated__Float.md) | **[[ReplicatedForwardInput]]**  |
| [FReplicated_Bool](/docs/SDK/Source/Classes/structFReplicated__Bool.md) | **[[ReplicatedIsAccelerating]]**  |
| [FReplicated_Bool](/docs/SDK/Source/Classes/structFReplicated__Bool.md) | **[[ReplicatedIsDecelerating]]**  |
| [FReplicated_Float](/docs/SDK/Source/Classes/structFReplicated__Float.md) | **[[ReplicatedRightInput]]**  |
| [FReplicated_Float](/docs/SDK/Source/Classes/structFReplicated__Float.md) | **[[ReplicatedTargetSpeed]]**  |
| float | **[[TargetSpeed]]**  |
| [FHorseMovementScale](/docs/SDK/Source/Classes/structFHorseMovementScale.md) | **[[TurnRateScale]]**  |
| [FTurnTowardsCameraParams](/docs/SDK/Source/Classes/structFTurnTowardsCameraParams.md) | **[[TurnTowardsCameraParams]]**  |
| bool | **[[bDebugAutoRun]]**  |
| bool | **[[bForceRun]]**  |
| bool | **[[bIsAccelerating]]**  |
| bool | **[[bIsDecelerating]]**  |
| bool | **[[bUseCruisingSpeed]]**  |
| bool | **[[bWantsToGallop]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| float | **[[BackwardsStrafeAngle]]**  |
| float | **[[BaseTurnRate]]**  |
| [FHorseMovementBlend](/docs/SDK/Source/Classes/structFHorseMovementBlend.md) | **[[BlendMovementState]]**  |
| bool | **[[BoostMode]]**  |
| float | **[[BreakingOrientationSpeed]]**  |
| float | **[[BreakingToReverseDelay]]**  |
| float | **[[CanInstantKickSpeed]]**  |
| float | **[[CanSlowDownToKickSpeed]]**  |
| bool | **[[ControlMode]]**  |
| TArray< float > | **[[CurveSections]]**  |
| float | **[[DashCooldown]]**  |
| float | **[[EmergencyBrakeSpeed]]**  |
| UPrimitiveComponent * | **[[FallingCollisionComponent]]**  |
| UCurveFloat * | **[[ForwardAngleToTurnMultiplierCurve]]**  |
| UCurveFloat * | **[[ForwardSpeedToStrafeSpeedCurve]]**  |
| float | **[[GamepadExclusiveHorizontalInputAngle]]**  |
| float | **[[GamepadExclusiveSagitalInputAngle]]**  |
| float | **[[GamepadInputOuterThreshold]]**  |
| UCurveFloat * | **[[GamepadInputToAxisMagnitudeCurve]]**  |
| TMap< TWeakObjectPtr< AActor >, float > | **[[HitActors]]**  |
| [FHorseBumpSettings](/docs/SDK/Source/Classes/structFHorseBumpSettings.md) | **[[HorseBumpSettings]]**  |
| [FHorseImpactRules](/docs/SDK/Source/Classes/structFHorseImpactRules.md) | **[[HorseImpactRules]]**  |
| [FHorseImpactSpeedSettings](/docs/SDK/Source/Classes/structFHorseImpactSpeedSettings.md) | **[[HorseImpactSpeedSettings]]**  |
| [FHorseToCharacterImpactSettings](/docs/SDK/Source/Classes/structFHorseToCharacterImpactSettings.md) | **[[HorseToCharacterImpactSettings]]**  |
| [FHorseToHorseImpactSettings](/docs/SDK/Source/Classes/structFHorseToHorseImpactSettings.md) | **[[HorseToHorseImpactSettings]]**  |
| EHorseToHorseImpactType | **[[HorseToHorseImpactType]]**  |
| [FHorseToWorldImpactSettings](/docs/SDK/Source/Classes/structFHorseToWorldImpactSettings.md) | **[[HorseToWorldImpactSettings]]**  |
| UCurveFloat * | **[[IdleAngleToTurnMultiplierCurve]]**  |
| float | **[[ImpactCooldown]]**  |
| FHitResult | **[[ImpactHitResult]]**  |
| float | **[[ImpactHitStrafe]]**  |
| float | **[[ImpactHitTime]]**  |
| EHorseImpactLocation | **[[ImpactLocation]]**  |
| float | **[[InertiaStrafeTime]]**  |
| UCurveFloat * | **[[InertiaStrafeTurnDecelCurve]]**  |
| UCurveFloat * | **[[InertiaTurnDecelCurve]]**  |
| float | **[[InertiaTurnTime]]**  |
| float | **[[InputDoubleTapThreshold]]**  |
| TMap< FName, [FHorseInputState](/docs/SDK/Source/Classes/structFHorseInputState.md) > | **[[InputState]]**  |
| float | **[[InputTapThreshold]]**  |
| UCurveFloat * | **[[InputTimeToMultiplierCurve]]**  |
| FName | **[[LastHorizontalInput]]**  |
| float | **[[LastLandedTime]]**  |
| float | **[[LookTurnPercentage]]**  |
| AActor * | **[[MaintainHorseSpeedOnImpact]]**  |
| FName | **[[MaxMovementState]]**  |
| float | **[[MaxSlowdownToKickTime]]**  |
| UDataTable * | **[[MovementDataTable]]**  |
| [FHorseMovementInput](/docs/SDK/Source/Classes/structFHorseMovementInput.md) | **[[MovementInput]]**  |
| [UMovementModifierComponent](/docs/SDK/Source/Classes/classUMovementModifierComponent.md) * | **[[MovementModifiers]]**  |
| float | **[[MovementStateDeltaTime]]**  |
| float | **[[MovementTransitionTime]]**  |
| [FOverrideForwardSpeed](/docs/SDK/Source/Classes/structFOverrideForwardSpeed.md) | **[[OverrideForwardSpeed]]**  |
| [FOverrideMaxSpeed](/docs/SDK/Source/Classes/structFOverrideMaxSpeed.md) | **[[OverrideMaxSpeed]]**  |
| [FOverrideTurnRate](/docs/SDK/Source/Classes/structFOverrideTurnRate.md) | **[[OverrideTurnRate]]**  |
| float | **[[PercentMaintainVelocityOnLanded]]**  |
| FName | **[[PreMovementState]]**  |
| [FHorseMovementInput](/docs/SDK/Source/Classes/structFHorseMovementInput.md) | **[[PreviousMovementInput]]**  |
| FName | **[[PreviousMovementState]]**  |
| FName | **[[SlowDownToKickAttackName]]**  |
| float | **[[SlowdownToEmoteSpeed]]**  |
| UCurveFloat * | **[[SpeedToForwardDecelCurve]]**  |
| UCurveFloat * | **[[SpeedToForwardDecelEmergency]]**  |
| UCurveFloat * | **[[SpeedToForwardDecelWhileStrafingCurve]]**  |
| UCurveFloat * | **[[SpeedToTurnRateCurve]]**  |
| TArray< FName > | **[[StandardMovementStates]]**  |
| UCurveFloat * | **[[StrafeAngleToTurnMultiplierCurve]]**  |
| UCurveFloat * | **[[StrafeToTurnRateCurve]]**  |
| float | **[[StrafeTurnMultiplier]]**  |
| int32 | **[[StuckPenetratingDirection]]**  |
| float | **[[TargetOrientationMax]]**  |
| float | **[[TargetOrientationMin]]**  |
| float | **[[TurnAgainstWallResistance]]**  |
| uint8 | **[[bBackwardStrafeAngleRelativeToCamera]]**  |
| bool | **[[bDidImpact]]**  |
| bool | **[[bDoStrafeOrbiting]]**  |
| uint8 | **[[bInvertBackwardsStrafe]]**  |
| bool | **[[bIsAdjustingFloorHeight]]**  |
| uint8 | **[[bIsDashDisabled]]**  |
| bool | **[[bIsEmergencyBrake]]**  |
| bool | **[[bIsStepUp]]**  |
| bool | **[[bIsStrafing]]**  |
| bool | **[[bNeedToRepressKeyForReverse]]**  |
| bool | **[[bRevertStepUpMovement]]**  |
| bool | **[[bStuckPenetrating]]**  |
| bool | **[[bSyncMaintainImpactSpeed]]**  |
| bool | **[[bUseBreakingState]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200