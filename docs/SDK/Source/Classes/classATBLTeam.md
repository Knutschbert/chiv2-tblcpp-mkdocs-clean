---
title: ATBLTeam
type: class
aliases: ATBLTeam
share: false

---

# ATBLTeam





Inherits from AInfo

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[[ATBLTeam]]**() |
| void | **[[BroadcastChat]]**(AActor * Sender, const FString & Msg, TEnumAsByte< EChatType::Type > Type) |
| void | **[[BroadcastLocalizedChat]]**(const FText & Msg, TEnumAsByte< EChatType::Type > Type) |
| void | **[[CommitRoundResult]]**(bool bWonRound) |
| virtual void | **[[GetLifetimeReplicatedProps]]**(TArray< FLifetimeProperty > & OutLifetimeProps) const override |
| float | **[[GetTeamScore]]**() const |
| void | **[[IncrementKills]]**(int32 Delta) |
| void | **[[SetTeamMaxTickets]]**(float MaxNumTickets) |
| void | **[[SetTeamScore]]**([FTeamScoreEvent](/docs/SDK/Source/Classes/structFTeamScoreEvent.md) ScoreEvent) |
| void | **[[SetTeamTickets]]**(float NewTickets) |
| void | **[[SetTiebreakScore]]**(float SecondaryScore) |
| void | **[[SwapWithTeam]]**([ATBLTeam](/docs/SDK/Source/Classes/classATBLTeam.md) * Other) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [FTeamDisplayInfo](/docs/SDK/Source/Classes/structFTeamDisplayInfo.md) | **[[DisplayInfo]]**  |
| EFaction | **[[Faction]]**  |
| float | **[[Kills]]**  |
| int32 | **[[MaxNumPlayers]]**  |
| float | **[[MaxTickets]]**  |
| TArray< TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > > | **[[PawnClasses]]**  |
| TArray< TSubclassOf< [ATBLCharacter](/docs/SDK/Source/Classes/classATBLCharacter.md) > > | **[[PawnSubclasses]]**  |
| TArray< [FRoundResult](/docs/SDK/Source/Classes/structFRoundResult.md) > | **[[RoundResults]]**  |
| int32 | **[[RoundsWon]]**  |
| float | **[[Tickets]]**  |
| float | **[[TiebreakScore]]**  |
| bool | **[[bIsTeamAttacking]]**  |
| bool | **[[bIsTeamDefending]]**  |

-------------------------------

Updated on 2023-07-04 at 02:30:59 +0200