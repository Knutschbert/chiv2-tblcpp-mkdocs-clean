---
title: UBreakableComponent
type: class
aliases: UBreakableComponent
share: false

---

# UBreakableComponent





Inherits from UActorComponent

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[[Damaged]]**(const [FDamageTakenEvent](/docs/SDK/Source/Classes/structFDamageTakenEvent.md) & Event) |
| void | **[[HealthStatChanged]]**(float Amount, AActor * Initiator) |
| void | **[[Killed]]**(const [FDeathDamageTakenEvent](/docs/SDK/Source/Classes/structFDeathDamageTakenEvent.md) & Event) |
| void | **[[SetFriendlyTeam]]**(EFaction InFriendlyTeam) |
| void | **[[SetHealth]]**(float InHealth) |
| | **[[UBreakableComponent]]**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| FVector | **[[FocalPointOffset]]**  |
| EFaction | **[[FriendlyTeam]]**  |
| TWeakObjectPtr< [UTBLGameScoringComponent](/docs/SDK/Source/Classes/classUTBLGameScoringComponent.md) > | **[[GameScoringComponent]]**  |
| float | **[[MaxHealth]]**  |
| FBreakableThresholdReached | **[[OnBreakableThresholdReached]]**  |
| FBreakableOnDamageTakenSignature | **[[OnDamageTaken]]**  |
| FBreakableOnKilledSignature | **[[OnKilled]]**  |
| [FStageActorAction](/docs/SDK/Source/Classes/structFStageActorAction.md) | **[[StageActorAction]]**  |
| float | **[[StartingHealth]]**  |
| TWeakObjectPtr< [UStatsComponent](/docs/SDK/Source/Classes/classUStatsComponent.md) > | **[[StatsComponent]]**  |
| TWeakObjectPtr< [UTeamOwnershipComponent](/docs/SDK/Source/Classes/classUTeamOwnershipComponent.md) > | **[[TeamOwnershipComponent]]**  |
| TArray< [FBreakableThreshold](/docs/SDK/Source/Classes/structFBreakableThreshold.md) > | **[[ThresholdsWithObjects]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200