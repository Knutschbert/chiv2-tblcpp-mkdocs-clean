---
title: ATBLAIController
type: class
aliases: ATBLAIController
share: false

---

# ATBLAIController





Inherits from AAIController

Inherited by [ATBLAICombatController](/docs/SDK/Source/Classes/classATBLAICombatController.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[ATBLAIController]]**() |
| void | **[[AttemptReturnToNavMesh]]**() |
| bool | **[[CanPathFollow]]**() const |
| void | **[[DestroyController]]**(AController * Controller) |
| void | **[[DestroyControllerAndPawn]]**(AController * Controller, APawn * TargetPawn) |
| void | **[[Dismount]]**() |
| AActor * | **[[GetTarget]]**() |
| float | **[[GetTargetMaxDistance]]**() |
| void | **[[GiveWeapon]]**(FName Weapon) |
| bool | **[[IsBackfillBot]]**() |
| bool | **[[IsDummyBot]]**() const |
| bool | **[[IsLevelSpawnedBot]]**() |
| bool | **[[IsOnNavMesh]]**() const |
| void | **[[Jump]]**() |
| void | **[[LogError]]**(FName ErrorType, const FString & Message, bool bError) |
| void | **[[LogEvent]]**(FName EventName, AActor * Target, const FString & DebugStr) |
| void | **[[MoveInput]]**(FVector2D InputDir, float Time, bool bAllowPathing) |
| bool | **[[MoveToNavMesh]]**(FVector PathGoal, AActor * PathGoalActor) |
| bool | **[[MoveToTargetLocation]]**(FVector Target) |
| void | **[[ResetError]]**(FName ErrorType) |
| void | **[[ReturnToNavMeshExpired]]**() |
| void | **[[SetBackfillBot]]**(bool bBackfill) |
| void | **[[SetDummyBot]]**(bool bDummy) |
| void | **[[SetNullBot]]**(bool bNull) |
| void | **[[SetTargetMaxDistance]]**(float MaxDistance) |
| void | **[[StopReturnToNavMesh]]**() |
| void | **[[StopUsingInteractable]]**() |
| void | **[[Suicide]]**() |
| void | **[[UseInteractable]]**([UInteractableComponent](/docs/SDK/Source/Classes/classUInteractableComponent.md) * Interactable, bool bHold) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| TArray< [FAIEventLog](/docs/SDK/Source/Classes/structFAIEventLog.md) > | **[[AIEventLog]]**  |
| int32 | **[[BotId]]**  |
| FString | **[[BotName]]**  |
| [UAIControlHandler](/docs/SDK/Source/Classes/classUAIControlHandler.md) * | **[[ControlHandler]]**  |
| [UInteractableComponent](/docs/SDK/Source/Classes/classUInteractableComponent.md) * | **[[CurrentlyUsedInteractable]]**  |
| UBehaviorTree * | **[[DefaultBehaviorTree]]**  |
| [UUtilityAI_DecisionMaker](/docs/SDK/Source/Classes/classUUtilityAI__DecisionMaker.md) * | **[[GeneralDecisionMakerComponent]]**  |
| float | **[[IdleTime]]**  |
| [UInputReplayComponent](/docs/SDK/Source/Classes/classUInputReplayComponent.md) * | **[[InputReplayComponent]]**  |
| bool | **[[IsInteractableUseBeingHeld]]**  |
| FVector | **[[MoveToNavMeshTarget]]**  |
| TMap< AActor *, int32 > | **[[NumTimesTargetted]]**  |
| FOnFailedToSpawn | **[[OnFailedToSpawn]]**  |
| FAIUsingInteractable | **[[OnInteractableStartedToBeHeld]]**  |
| FAIUsingInteractable | **[[OnInteractableStoppedBeingHeld]]**  |
| FAIUsingInteractable | **[[OnInteractableUsed]]**  |
| FAIPossessedPawnSignature | **[[OnPossessedPawn]]**  |
| FOnPawnPendingDestroy | **[[OnPossessedPawnPendingDestroy]]**  |
| FOnStartedBehaviorTree | **[[OnStartedBehaviorTree]]**  |
| [ATBLPlayerController](/docs/SDK/Source/Classes/classATBLPlayerController.md) * | **[[OverridePlayerController]]**  |
| [FAIPersonality](/docs/SDK/Source/Classes/structFAIPersonality.md) | **[[Personality]]**  |
| FName | **[[PersonalityRowOverride]]**  |
| UDataTable * | **[[PersonalityTable]]**  |
| TArray< TEnumAsByte< EAudioPersonalityType::Type > > | **[[PossiblePersonalities]]**  |
| [AAIPlayerStart](/docs/SDK/Source/Classes/classAAIPlayerStart.md) * | **[[SpawnPoint]]**  |
| bool | **[[bCreatePlayerState]]**  |
| bool | **[[bIsLevelSpawnedBot]]**  |
| bool | **[[bIsPlayerCustomizedBot]]**  |
| bool | **[[bOverridePersonalityRow]]**  |
| bool | **[[bOverrideRotation]]**  |
| bool | **[[bUseCrowdManager]]**  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| TArray< FName > | **[[LoggedErrorTypes]]**  |
| FVector2D | **[[MoveInputDirection]]**  |
| float | **[[MoveInputTime]]**  |
| int32 | **[[NavMeshReturnAttemptCount]]**  |
| FTimerHandle | **[[NavMeshReturnAttemptHandle]]**  |
| FVector | **[[PreviousLocation]]**  |
| FVector | **[[SpawnLocation]]**  |
| FRotator | **[[SpawnRotation]]**  |
| float | **[[TargetMaxDistance]]**  |
| bool | **[[bAllowPathingWithMoveInput]]**  |
| bool | **[[bBackfillBot]]**  |
| bool | **[[bDummyBot]]**  |
| bool | **[[bNullBot]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:58 +0200