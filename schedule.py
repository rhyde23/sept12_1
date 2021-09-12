#Schedule
import random
from stadiums import get_stadium

schedule_prem = """
Saturday 12 September
12:30 Fulham v Arsenal (BT Sport)
15:00 Crystal Palace v Southampton (BT Sport)
17:30 Liverpool v Leeds (Sky Sports)
20:00 West Ham v Newcastle (Sky Sports)

Sunday 13 September
14:00 West Brom v Leicester (Sky Sports)
16:30 Spurs v Everton (Sky Sports)

Monday 14 September
18:00 Sheffield Utd v Wolves (Sky Sports)
20:15 Brighton v Chelsea (Sky Sports)

Saturday 19 September
12:30 Everton v West Brom (BT Sport)
15:00 Leeds v Fulham (BT Sport)
17:30 Man Utd v Crystal Palace (Sky Sports)
20:00 Arsenal v West Ham (Sky Sports)

Sunday 20 September
12:00 Southampton v Spurs (BT Sport)
14:00 Newcastle v Brighton (Sky Sports)
16:30 Chelsea v Liverpool (Sky Sports)
19:00 Leicester v Burnley (BBC Sport)

Monday 21 September
18:00 Aston Villa v Sheffield Utd (Sky Sports)
20:15 Wolves v Man City (Sky Sports)

Saturday 26 September
12:30 Brighton v Man Utd (BT Sport)
15:00 Crystal Palace v Everton (Amazon Prime)
17:30 West Brom v Chelsea (Sky Sports)
20:00 Burnley v Southampton (Sky Sports)

Sunday 27 September
12:00 Sheffield Utd v Leeds (BT Sport)
14:00 Spurs v Newcastle (Sky Sports)
16:30 Man City v Leicester (Sky Sports)
19:00 West Ham v Wolves (BT Sport)

Monday 28 September
17:45 Fulham v Aston Villa (Sky Sports)
20:00 Liverpool v Arsenal (Sky Sports) 

Saturday 3 October
12:30 Chelsea v Crystal Palace (BT Sport)
15:00 Everton v Brighton (BT Sport)
17:30 Leeds v Man City (Sky Sports)
20:00 Newcastle v Burnley (Sky Sports)

Sunday 4 October 
12:00 Leicester v West Ham (BT Sport)
12:00 Southampton v West Brom (BT Sport)
14:00 Arsenal v Sheffield Utd (Sky Sports)
14:00 Wolves v Fulham (Sky Sports)
16:30 Man Utd v Spurs (Sky Sports)
19:15 Aston Villa v Liverpool (Sky Sports)

Saturday 17 October
12:30 Everton v Liverpool (BT Sport)
15:00 Chelsea v Southampton (BT Sport Box Office)
17:30 Man City v Arsenal (Sky Sports)
20:00 Newcastle v Man Utd (Sky Sports Box Office)

Sunday 18 October
12:00 Sheffield Utd v Fulham (BT Sport Box Office)
14:00 Crystal Palace v Brighton (Sky Sports)
16:30 Spurs v West Ham (Sky Sports)
19:15 Leicester v Aston Villa (Sky Sports Box Office)

Monday 19 October
17:30 West Brom v Burnley (Sky Sports Box Office)
20:00 Leeds v Wolves (Sky Sports)

Friday 23 October
20:00 Aston Villa v Leeds

Saturday 24 October
12:30 West Ham v Man City (BT Sport)
15:00 Fulham v Crystal Palace (BT Sport Box Office)
17:30 Man Utd v Chelsea (Sky Sports)
20:00 Liverpool v Sheffield Utd (Sky Sports Box Office)

Sunday 25 October
14:00 Southampton v Everton (Sky Sports)
16:30 Wolves v Newcastle (Sky Sports)
19:15 Arsenal v Leicester (Sky Sports Box Office)

Monday 26 October
17:30 Brighton v West Brom (Sky Sports Box Office)
20:00 Burnley v Spurs (Sky Sports)

Friday 30 October
20:00 Wolves v Crystal Palace (BT Sport Box Office)

Saturday 31 October
12:30 Sheffield Utd v Man City (BT Sport)
15:00 Burnley v Chelsea (BT Sport Box Office)
17:30 Liverpool v West Ham (Sky Sports)

Sunday 1 November
12:00 Aston Villa v Southampton (Sky Sports Box Office)
14:00 Newcastle v Everton (Sky Sports)
16:30 Man Utd v Arsenal (Sky Sports)
19:15 Spurs v Brighton (Sky Sports Box Office)

Monday 2 November
17:30 Fulham v West Brom (Sky Sports Box Office)
20:00 Leeds v Leicester (Sky Sports)

Friday 6 November
17:30 Brighton v Burnley (Sky Sports Box Office)
20:00 Southampton v Newcastle (Sky Sports)

Saturday 7 November
12:30 Everton v Man Utd (BT Sport)
15:00 Crystal Palace v Leeds (BT Sport Box Office)
17:30 Chelsea v Sheffield Utd (Sky Sports)
20:00 West Ham v Fulham (BT Sport Box Office)

Sunday 8 November
12:00 West Brom v Spurs (Sky Sports Box Office)
14:00 Leicester v Wolves (Sky Sports)
16:30 Man City v Liverpool (Sky Sports)
19:15 Arsenal v Aston Villa (Sky Sports Box Office)

Saturday 21 November
12:30 Newcastle v Chelsea (BT Sport)
15:00 Aston Villa v Brighton (BT Sport)
17:30 Spurs v Man City (Sky Sports)
20:00 Man Utd v West Brom (BT Sport) 

Sunday 22 November
12:00 Fulham v Everton (BBC Sport)
14:00 Sheffield Utd v West Ham (Sky Sports)
16:30 Leeds v Arsenal (Sky Sports)
19:15 Liverpool v Leicester (Sky Sports)

Monday 23 November
17:30 Burnley v Crystal Palace (Sky Sports)
20:00 Wolves v Southampton (Sky Sports)

Friday 27 November
20:00 Crystal Palace v Newcastle (Amazon Prime Video)

Saturday 28 November
12:30 Brighton v Liverpool (BT Sport)
15:00 Man City v Burnley (BT Sport)
17:30 Everton v Leeds (Sky Sports)
20:00 West Brom v Sheffield Utd (Sky Sports)

Sunday 29 November
14:00 Southampton v Man Utd (Sky Sports)
16:30 Chelsea v Spurs (Sky Sports)
19:15 Arsenal v Wolves (Sky Sports)

Monday 30 November
17:30 Leicester v Fulham (Sky Sports)
20:00 West Ham v Aston Villa (Sky Sports)

Friday 4 December
20:00 Aston Villa v Newcastle (Sky Sports)

Saturday 5 December
12:30 Burnley v Everton (BT Sport)
15:00 Man City v Fulham (BT Sport)
17:30 West Ham v Man Utd (Sky Sports)
20:00 Chelsea v Leeds (Sky Sports)

Sunday 6 December
12:00 West Brom v Crystal Palace (Sky Sports)
14:15 Sheffield Utd v Leicester (Sky Sports)
16:30 Spurs v Arsenal (Sky Sports)
19:15 Liverpool v Wolves (Amazon Prime Video)

Monday 7 December
20:00 Brighton v Southampton (Sky Sports)

Friday 11 December
20:00 Leeds v West Ham (Sky Sports)

Saturday 12 December
12:30 Wolves v Aston Villa (BT Sport)
15:00 Newcastle v West Brom (Sky Sports)
17:30 Man Utd v Man City (Sky Sports)
20:00 Everton v Chelsea (BT Sport) 

Sunday 13 December
12:00 Southampton v Sheff Utd (Sky Sports)
14:15 Crystal Palace v Spurs (Sky Sports)
16:30 Fulham v Liverpool (Sky Sports)
19:15 Arsenal v Burnley (Sky Sports)
19:15 Leicester v Brighton (Amazon Prime Video)

Tuesday 15 December
18:00 Wolves v Chelsea (Amazon Prime Video)
20:00 Man City v West Brom (Amazon Prime Video)

Wednesday 16 December
18:00 Arsenal v Southampton (Amazon Prime Video)
18:00 Leeds v Newcastle (Amazon Prime Video)
18:00 Leicester v Everton (Amazon Prime Video)
20:00 Fulham v Brighton (Amazon Prime Video)
20:00 Liverpool v Spurs (Amazon Prime Video)
20:00 West Ham v Crystal Palace (Amazon Prime Video)

Thursday 17 December
18:00 Aston Villa v Burnley (Amazon Prime Video)
20:00 Sheffield Utd v Man Utd (Amazon Prime Video)

Saturday 19 December
12:30 Crystal Palace v Liverpool (BT Sport)
15:00 Southampton v Man City (Amazon Prime Video)
17:30 Everton v Arsenal (Sky Sports)
20:00 Newcastle v Fulham (Sky Sports)

Sunday 20 December
12:00 Brighton v Sheffield Utd (Sky Sports)
14:15 Spurs v Leicester (Sky Sports)
16:30 Man Utd v Leeds (Sky Sports)
19:15 West Brom v Aston Villa (BT Sport)

Monday 21 December
17:30 Burnley v Wolves (Sky Sports)
20:00 Chelsea v West Ham (Sky Sports)

Saturday 26 December
12:30 Leicester v Man Utd (BT Sport)
15:00 Aston Villa v Crystal Palace (BBC)
15:00 Fulham v Southampton (Sky Sports)
17:30 Arsenal v Chelsea (Sky Sports)
20:00 Man City v Newcastle (BT Sport)
20:00 Sheffield Utd v Everton (BT Sport)

Sunday 27 December
12:00 Leeds v Burnley (Sky Sports)
14:15 West Ham v Brighton (Sky Sports)
16:30 Liverpool v West Brom (Sky Sports)
19:15 Wolves v Spurs (Sky Sports)

Monday 28 December
15:00 Crystal Palace v Leicester (Amazon Prime Video)
17:30 Chelsea v Aston Villa (Amazon Prime Video)
20:00 Everton v Man City (Amazon Prime Video)

Tuesday 29 December
18:00 Brighton v Arsenal (Amazon Prime Video)
18:00 Burnley v Sheffield Utd (Amazon Prime Video)
18:00 Southampton v West Ham (Amazon Prime Video)
18:00 West Brom v Leeds (Amazon Prime Video)
20:00 Man Utd v Wolves (Amazon Prime Video)

Wednesday 30 December
18:00 Spurs v Fulham (Amazon Prime Video)
20:00 Newcastle v Liverpool (Amazon Prime Video)

Friday 1 January
17:30 Everton v West Ham (BT Sport)
20:00 Man Utd v Aston Villa (Sky Sports)

Saturday 2 January
12:30 Spurs v Leeds (BT Sport)
15:00 Crystal Palace v Sheff Utd (Sky Sports)
17:30 Brighton v Wolves (Sky Sports)
20:00 West Brom v Arsenal (BT Sport)

Sunday 3 January
12:00 Burnley v Fulham (Sky Sports)
14:15 Newcastle v Leicester (Sky Sports)
16:30 Chelsea v Man City (Sky Sports)

Monday 4 January
20:00 Southampton v Liverpool (Sky Sports)

*Matchweek 18 fixtures have been split between 12-14 January and 19-21 January and are signified by an asterisk.

Tuesday 12 January
18:00 Sheff Utd v Newcastle (Sky Sports)*
20:15 Wolves v Everton (Sky Sports)*
20:15 Burnley v Man Utd (Sky Sports)

Wednesday 13 January
18:00 Man City v Brighton (BT Sport)*
20:15 Aston Villa v Spurs (Sky Sports)*

Thursday 14 January
20:00 Arsenal v Crystal Palace (Sky Sports)*

Friday 15 January
20:00 Fulham v Chelsea (Sky Sports)

Saturday 16 January
12:30 Wolves v West Brom (BT Sport)
15:00 Leeds v Brighton (Sky Sports)
15:00 West Ham v Burnley (Amazon Prime)
17:30 Aston Villa v Everton (Sky Sports)
20:00 Leicester v Southampton (BT Sport)

Sunday 17 January
14:00 Sheffield Utd v Spurs (Sky Sports)
16:30 Liverpool v Man Utd (Sky Sports)
19:15 Man City v Crystal Palace (Sky Sports)

Monday 18 January
20:00 Arsenal v Newcastle (Sky Sports)

Tuesday 19 January
18:00 West Ham v West Brom (BT Sport)*
20:15 Leicester v Chelsea (Sky Sports)*

Wednesday 20 January
18:00 Man City v Aston Villa (BT Sport)
20:15 Fulham v Man Utd (BT Sport)*

Thursday 21 January
20:00 Liverpool v Burnley (Sky Sports)*

Saturday 23 January
20:00 Aston Villa v Newcastle (Sky Sports)

Tuesday 26 January
18:00 Crystal Palace v West Ham (BT Sport)
18:00 Newcastle v Leeds (BT Sport)
20:15 Southampton v Arsenal (BT Sport)
20:15 West Brom v Man City (BT Sport)

Wednesday 27 January
18:00 Burnley v Aston Villa (BT Sport)
18:00 Chelsea v Wolves (BT Sport)
19:30 Brighton v Fulham (BT Sport) 
20:15 Everton v Leicester (BT Sport)
20:15 Man Utd v Sheffield Utd (BT Sport)

Thursday 28 January
20:00 Spurs v Liverpool (BT Sport)

Saturday 30 January
12:30 Everton v Newcastle (BT Sport)
15:00 Crystal Palace v Wolves (Sky Sports)
15:00 Man City v Sheffield Utd (Sky Sports)
15:00 West Brom v Fulham (BT Sports)
17:30 Arsenal v Man Utd (Sky Sports)
20:00 Southampton v Aston Villa (Sky Sports)

Sunday 31 January
12:00 Chelsea v Burnley (BT Sport)
14:00 Leicester v Leeds (Sky Sports)
16:30 West Ham v Liverpool (Sky Sports)
19:15 Brighton v Spurs (Sky Sports)

Tuesday 2 February 
18:00 Sheffield Utd v West Brom (BT Sport)
18:00 Wolves v Arsenal (BT Sport)
20:15 Man Utd v Southampton (BT Sport)
20:15 Newcastle v Crystal Palace (BT Sport)

Wednesday 3 February
18:00 Burnley v Man City (BT Sport)
18:00 Fulham v Leicester (BT Sport)
19:30 Leeds v Everton (BT Sport)
20:15 Aston Villa v West Ham (BT Sport)
20:15 Liverpool v Brighton (BT Sport)

Thursday 4 February
20:00 Spurs v Chelsea (BT Sport)

Saturday 6 February
12:30 Aston Villa v Arsenal (BT Sport)
15:00 Burnley v Brighton (Sky Sports)
15:00 Newcastle v Southampton (BT Sport)
17:30 Fulham v West Ham (Sky Sports)
20:00 Man Utd v Everton (Sky Sports)*
(*moved from 8 Feb for FA Cup match) 

Sunday 7 February
12:00 Spurs v West Brom (BT Sport)
14:00 Wolves v Leicester (Sky Sports)
16:30 Liverpool v Man City (Sky Sports)
19:15 Sheffield Utd v Chelsea (Sky Sports)

Monday 8 February 
20:00 Leeds v Crystal Palace (Sky Sports)

Saturday 13 February
12:30 Leicester v Liverpool (BT Sport)
15:00 Crystal Palace v Burnley (Sky Sports)
17:30 Man City v Spurs (Sky Sports)
20:00 Brighton v Aston Villa (Sky Sports)

Sunday 14 February 
12:00 Southampton v Wolves (Amazon Prime)
14:00 West Brom v Man Utd (Sky Sports)
16:30 Arsenal v Leeds (Sky Sports)
19:00 Everton v Fulham (BT Sport)

Monday 15 February 
18:00 West Ham v Sheffield Utd (BT Sport)
20:00 Chelsea v Newcastle (Sky Sports)

Wednesday 17 February 
18:00 Burnley v Fulham (Sky Sports)
20:15 Everton v Man City (Amazon Prime)

Friday 19 February 
20:00 Wolves v Leeds (BT Sport)

Saturday 20 February
12:30 Southampton v Chelsea (BT Sport)
15:00 Burnley v West Brom (Sky Sports)
17:30 Liverpool v Everton (Sky Sports)
20:00 Fulham v Sheffield Utd (Sky Sports)

Sunday 21 February 
12:00 West Ham v Spurs (Sky Sports)
14:00 Aston Villa v Leicester (Sky Sports)
16:30 Arsenal v Man City (Sky Sports)
19:00 Man Utd v Newcastle (BT Sport)

Monday 22 February 
20:00 Brighton v Crystal Palace (Sky Sports)

Tuesday 22 February 
18:00 Leeds v Southampton (Sky Sports)

Saturday 27 February
12:30 Man City v West Ham (BT Sport)
15:00 West Brom v Brighton (Sky Sports)
17:30 Leeds v Aston Villa (Sky Sports)
20:00 Newcastle v Wolves (Sky Sports)

Sunday 28 February
12:00 Crystal Palace v Fulham (BBC)
12:00 Leicester v Arsenal (BT Sport)
14:00 Spurs v Burnley (Sky Sports)
16:30 Chelsea v Man Utd (Sky Sports)
19:15 Sheffield Utd v Liverpool (Sky Sports)

Monday 1 March 
20:00 Everton v Southampton (Sky Sports)

Tuesday 2 March
20:00 Man City v Wolves (BT Sport)

Wednesday 3 March
18:00 Burnley v Leicester (Sky Sports)
18:00 Sheff Utd v Aston Villa (BT Sport)
20:15 Crystal Palace v Man Utd (Sky Sports)

Thursday 4 March
18:00 Fulham v Spurs (BT Sport)
18:00 West Brom v Everton (Sky Sports)
20:15 Liverpool v Chelsea (Sky Sports)

Saturday 6 March
12:30 Burnley v Arsenal (BT Sport)
15:00 Sheff Utd v Southampton (Sky Sports)
17:30 Aston Villa v Wolves (Sky Sports)
20:00 Brighton v Leicester (Sky Sports)

Sunday 7 March
12:00 West Brom v Newcastle (Amazon Prime)
14:00 Liverpool v Fulham (Sky Sports)
16:30 Man City v Man Utd (Sky Sports)
19:15 Spurs v Crystal Palace (Sky Sports)

Monday 8 March
18:00 Chelsea v Everton (BT Sport)
20:00 West Ham v Leeds (Sky Sports)

Wednesday 10 March
18:00 Man City v Southampton (Sky Sports)

Friday 12 March
20:00 Newcastle v Aston Villa (BT Sport)

Saturday 13 March
12:30 Leeds v Chelsea (BT Sport)
15:00 Crystal Palace v West Brom (Sky Sports)
17:30 Everton v Burnley (Sky Sports)
20:00 Fulham v Man City (BT Sport)

Sunday 14 March
12:00 Southampton v Brighton (BBC)
14:00 Leicester v Sheffield United (Sky Sports)
16:30 Arsenal v Spurs (Sky Sports)
19:15 Man Utd v West Ham (Sky Sports)

Monday 15 March
20:00 Wolves v Liverpool (Sky Sports)

Friday 19 March
20:00 Fulham v Leeds (Sky Sports)

Saturday 20 March
20:00 Brighton v Newcastle (Sky Sports)

Sunday 21 March
15:00 West Ham v Arsenal (Sky Sports)
19:30 Aston Villa v Spurs (Sky Sports)

(all times BST)

Saturday 3 April
12:30 Chelsea v West Brom (BT Sport)
15:00 Leeds v Sheff Utd (Amazon Prime)
17:30 Leicester v Man City (Sky Sports)
20:00 Arsenal v Liverpool (Sky Sports)

Sunday 4 April
12:00 Southampton v Burnley (Sky Sports)
14:05 Newcastle v Spurs (Sky Sports)
16:30 Aston Villa v Fulham (Sky Sports) 
19:30 Man Utd v Brighton (BT Sport)

Monday 5 April
18:00 Everton v Crystal Palace (Sky Sports)
20:15 Wolves v West Ham (Sky Sports)

Friday 9 April
20:00 Fulham v Wolves (BT Sport)

Saturday 10 April
12:30 Man City v Leeds (BT Sport)
15:00 Liverpool v Aston Villa (Sky Sports)
17:30 Crystal Palace v Chelsea (Sky Sports)

Sunday 11 April
12:00 Burnley v Newcastle (Sky Sports)
14:05 West Ham v Leicester (Sky Sports)
16:30 Spurs v Man Utd (Sky Sports)
19:00 Sheff Utd v Arsenal (BT Sport)

Monday 12 April
18:00 West Brom v Southampton (Sky Sports)
20:15 Brighton v Everton (Sky Sports)

Friday 16 April
20:00 Everton v Spurs (Sky Sports)

Saturday 17 April
12:30 Newcastle v West Ham (Sky Sports)
20:15 Wolves v Sheff Utd (Sky Sports)

Sunday 18 April
13:30 Arsenal v Fulham (Sky Sports)
16:00 Man Utd v Burnley (Sky Sports)

Monday 19 April
20:00 Leeds v Liverpool (Sky Sports)

Tuesday 20 April
20:00 Chelsea v Brighton (Sky Sports)

Wednesday 21 April
18:00 Spurs v Southampton (Sky Sports)
20:15 Aston Villa v Man City (Sky Sports)

Thursday 22 April
20:00 Leicester v West Brom (BT Sport)

Friday 23 April
20:00 Arsenal v Everton (Sky Sports)

Saturday 24 April
12:30 Liverpool v Newcastle (BT Sport)
17:30 West Ham v Chelsea (Sky Sports)
20:00 Sheff Utd v Brighton (Sky Sports)

Sunday 25 April
12:00 Wolves v Burnley (BBC)
14:00 Leeds v Man Utd (Sky Sports)
19:00 Aston Villa v West Brom (BT Sport)

Monday 26 April
20:00 Leicester v Crystal Palace (Sky Sports)

Friday 30 April
20:00 Southampton v Leicester (Sky Sports)

Saturday 1 May
12:30 Crystal Palace v Man City (BT Sport)
15:00 Brighton v Leeds (Amazon Prime)
17:30 Chelsea v Fulham (Sky Sports)
20:00 Everton v Aston Villa (BT Sport)

Sunday 2 May
14:00 Newcastle v Arsenal (Sky Sports)
16:30 Man Utd v Liverpool (Sky Sports)
19:15 Spurs v Sheffield Utd (Sky Sports)

Monday 3 May
18:00 West Brom v Wolves (Sky Sports)
20:15 Burnley v West Ham (Sky Sports)

Friday 7 May
20:00 Leicester v Newcastle (Sky Sports)

Saturday 8 May
12:30 Leeds v Spurs (BT Sport)
15:00 Sheffield Utd v Crystal Palace (Sky Sports)
17:30 Man City v Chelsea (Sky Sports)
20:15 Liverpool v Southampton (Sky Sports)

Sunday 9 May
12:00 Wolves v Brighton (BBC)
14:05 Aston Villa v Man Utd (Sky Sports)
16:30 West Ham v Everton (Sky Sports)
19:00 Arsenal v West Brom (BT Sport)

Monday 10 May
20:00 Fulham v Burnley (Sky Sports)

Tuesday 11 May 
18:00 Man Utd v Leicester (BT Sport)
20:15 Southampton v Crystal Palace (Sky Sports)

Wednesday 12 May
20:15 Chelsea v Arsenal (Sky Sports)

Thursday 13 May 
18:00 Aston Villa v Everton (Sky Sports) 
20:15 Man Utd v Liverpool (Sky Sports)

Friday 14 May 
20:00 Newcastle v Man City (Sky Sports)

Saturday 15 May 
12:30 Burnley v Leeds (BT Sport)
15:00 Southampton v Fulham (Sky Sports)
20:00 Brighton v West Ham (Sky Sports)

Sunday 16 May
12:00 Crystal Palace v Aston Villa (Sky Sports)
14:05 Spurs v Wolves (Sky Sports)
16:30 West Brom v Liverpool (Sky Sports)
19:00 Everton v Sheff Utd (BT Sport)

Tuesday 18 May
18:00 Man Utd v Fulham (Sky Sports)
18:00 Southampton v Leeds (Sky Sports)
19:00 Brighton v Man City (BT Sport)
20:15 Chelsea v Leicester (Sky Sports)

Wednesday 19 May
18:00 Everton v Wolves (Sky Sports)
18:00 Newcastle v Sheff Utd (Sky Sports)
18:00 Spurs v Aston Villa (Sky Sports)
19:00 Crystal Palace v Arsenal (BT Sport)
20:15 Burnley v Liverpool (Sky Sports) 
20:15 West Brom v West Ham (Sky Sports)

Sunday 23 May
16:00 Arsenal v Brighton (Sky Sports Arena)
16:00 Aston Villa v Chelsea (Sky Sports Action)
16:00 Fulham v Newcastle (Sky Sports Mix)
16:00 Leeds v West Brom (BT Sport 2)
16:00 Leicester v Spurs (Sky Sports Football)
16:00 Liverpool v Crystal Palace (Sky Sports Main Event)
16:00 Man City v Everton (Sky Sports Premier League)
16:00 Sheffield Utd v Burnley (BT Sport 3)
16:00 West Ham v Southampton (Sky One)
16:00 Wolves v Man Utd (BT Sport 1)
"""

schedule_championship = """
Saturday, Sept. 12, 2020
A.F.C. Bournemouth v Blackburn Rovers
Barnsley v Luton Town
Birmingham City v Brentford
Bristol City v Coventry City
Cardiff City v Sheffield Wednesday
Derby County v Reading
Huddersfield Town v Norwich City
Millwall v Stoke City
Preston North End v Swansea City
Queens Park Rangers v Nottingham Forest
Watford v Middlesbrough
Wycombe Wanderers v Rotherham United

Saturday, Sept. 19, 2020
Blackburn Rovers v Wycombe Wanderers
Brentford v Huddersfield Town
Coventry City v Queens Park Rangers
Luton Town v Derby County
Middlesbrough v A.F.C. Bournemouth
Norwich City v Preston North End
Nottingham Forest v Cardiff City
Reading v Barnsley
Rotherham United v Millwall
Sheffield Wednesday v Watford
Stoke City v Bristol City
Swansea City v Birmingham City

Saturday, Sept. 26, 2020
A.F.C. Bournemouth v Norwich City
Barnsley v Coventry City
Birmingham City v Rotherham United
Bristol City v Sheffield Wednesday
Cardiff City v Reading
Derby County v Blackburn Rovers
Huddersfield Town v Nottingham Forest
Millwall v Brentford
Preston North End v Stoke City
Queens Park Rangers v Middlesbrough
Watford v Luton Town
Wycombe Wanderers v Swansea City

Saturday, Oct. 3, 2020
Blackburn Rovers v Cardiff City
Brentford v Preston North End
Coventry City v A.F.C. Bournemouth
Luton Town v Wycombe Wanderers
Middlesbrough v Barnsley
Norwich City v Derby County
Nottingham Forest v Bristol City
Reading v Watford
Rotherham United v Huddersfield Town
Sheffield Wednesday v Queens Park Rangers
Stoke City v Birmingham City
Swansea City v Millwall

Saturday, Oct. 17, 2020
A.F.C. Bournemouth v Queens Park Rangers
Barnsley v Bristol City
Birmingham City v Sheffield Wednesday
Blackburn Rovers v Nottingham Forest
Brentford v Coventry City
Derby County v Watford
Luton Town v Stoke City
Middlesbrough v Reading
Preston North End v Cardiff City
Rotherham United v Norwich City
Swansea City v Huddersfield Town
Wycombe Wanderers v Millwall

Tuesday, Oct. 20, 2020
Bristol City v Middlesbrough
Coventry City v Swansea City
Millwall v Luton Town
Norwich City v Birmingham City
Nottingham Forest v Rotherham United
Reading v Wycombe Wanderers

Wednesday, Oct. 21, 2020
Cardiff City v A.F.C. Bournemouth
Huddersfield Town v Derby County
Queens Park Rangers v Preston North End
Sheffield Wednesday v Brentford
Stoke City v Barnsley
Watford v Blackburn Rovers

Saturday, Oct. 24, 2020
Bristol City v Swansea City
Cardiff City v Middlesbrough
Coventry City v Blackburn Rovers
Huddersfield Town v Preston North End
Millwall v Barnsley
Norwich City v Wycombe Wanderers
Nottingham Forest v Derby County
Queens Park Rangers v Birmingham City
Reading v Rotherham United
Sheffield Wednesday v Luton Town
Stoke City v Brentford
Watford v A.F.C. Bournemouth

Tuesday, Oct. 27, 2020
Barnsley v Queens Park Rangers
Blackburn Rovers v Reading
Brentford v Norwich City
Middlesbrough v Coventry City
Swansea City v Stoke City
Wycombe Wanderers v Watford

Wednesday, Oct. 28, 2020
A.F.C. Bournemouth v Bristol City
Birmingham City v Huddersfield Town
Derby County v Cardiff City
Luton Town v Nottingham Forest
Preston North End v Millwall
Rotherham United v Sheffield Wednesday

Saturday, Oct. 31, 2020
A.F.C. Bournemouth v Derby County
Barnsley v Watford
Bristol City v Norwich City
Coventry City v Reading
Luton Town v Brentford
Middlesbrough v Nottingham Forest
Millwall v Huddersfield Town
Preston North End v Birmingham City
Queens Park Rangers v Cardiff City
Stoke City v Rotherham United
Swansea City v Blackburn Rovers
Wycombe Wanderers v Sheffield Wednesday

Tuesday, Nov. 3, 2020
Blackburn Rovers v Middlesbrough
Brentford v Swansea City
Cardiff City v Barnsley
Huddersfield Town v Bristol City
Norwich City v Millwall
Sheffield Wednesday v A.F.C. Bournemouth

Wednesday, Nov. 4, 2020
Birmingham City v Wycombe Wanderers
Derby County v Queens Park Rangers
Nottingham Forest v Coventry City
Reading v Preston North End
Rotherham United v Luton Town
Watford v Stoke City

Saturday, Nov. 7, 2020
Birmingham City v A.F.C. Bournemouth
Blackburn Rovers v Queens Park Rangers
Brentford v Middlesbrough
Cardiff City v Bristol City
Derby County v Barnsley
Huddersfield Town v Luton Town
Norwich City v Swansea City
Nottingham Forest v Wycombe Wanderers
Reading v Stoke City
Rotherham United v Preston North End
Sheffield Wednesday v Millwall
Watford v Coventry City

Saturday, Nov. 21, 2020
A.F.C. Bournemouth v Reading
Barnsley v Nottingham Forest
Bristol City v Derby County
Coventry City v Birmingham City
Luton Town v Blackburn Rovers
Middlesbrough v Norwich City
Millwall v Cardiff City
Preston North End v Sheffield Wednesday
Queens Park Rangers v Watford
Stoke City v Huddersfield Town
Swansea City v Rotherham United
Wycombe Wanderers v Brentford

Tuesday, Nov. 24, 2020
A.F.C. Bournemouth v Nottingham Forest
Barnsley v Brentford
Luton Town v Birmingham City
Preston North End v Blackburn Rovers
Queens Park Rangers v Rotherham United
Stoke City v Norwich City

Wednesday, Nov. 25, 2020
Bristol City v Watford
Coventry City v Cardiff City
Middlesbrough v Derby County
Millwall v Reading
Swansea City v Sheffield Wednesday
Wycombe Wanderers v Huddersfield Town

Saturday, Nov. 28, 2020
Birmingham City v Millwall
Blackburn Rovers v Barnsley
Brentford v Queens Park Rangers
Cardiff City v Luton Town
Derby County v Wycombe Wanderers
Huddersfield Town v Middlesbrough
Norwich City v Coventry City
Nottingham Forest v Swansea City
Reading v Bristol City
Rotherham United v A.F.C. Bournemouth
Sheffield Wednesday v Stoke City
Watford v Preston North End

Tuesday, Dec. 1, 2020
A.F.C. Bournemouth v Preston North End
Birmingham City v Barnsley
Cardiff City v Huddersfield Town
Derby County v Coventry City
Queens Park Rangers v Bristol City
Rotherham United v Brentford

Wednesday, Dec. 2, 2020
Blackburn Rovers v Millwall
Luton Town v Norwich City
Middlesbrough v Swansea City
Nottingham Forest v Watford
Sheffield Wednesday v Reading
Wycombe Wanderers v Stoke City

Saturday, Dec. 5, 2020
Barnsley v A.F.C. Bournemouth
Brentford v Blackburn Rovers
Bristol City v Birmingham City
Coventry City v Rotherham United
Huddersfield Town v Queens Park Rangers
Millwall v Derby County
Norwich City v Sheffield Wednesday
Preston North End v Wycombe Wanderers
Reading v Nottingham Forest
Stoke City v Middlesbrough
Swansea City v Luton Town
Watford v Cardiff City

Tuesday, Dec. 7, 2020
Coventry City v Luton Town
Huddersfield Town v Sheffield Wednesday
Millwall v Queens Park Rangers
Stoke City v Cardiff City
Swansea City v A.F.C. Bournemouth
Watford v Rotherham United

Wednesday, Dec. 8, 2020
Barnsley v Wycombe Wanderers
Brentford v Derby County
Bristol City v Blackburn Rovers
Norwich City v Nottingham Forest
Preston North End v Middlesbrough
Reading v Birmingham City

Saturday, Dec. 12, 2020
A.F.C. Bournemouth v Huddersfield Town
Birmingham City v Watford
Blackburn Rovers v Norwich City
Cardiff City v Swansea City
Derby County v Stoke City
Luton Town v Preston North End
Middlesbrough v Millwall
Nottingham Forest v Brentford
Queens Park Rangers v Reading
Rotherham United v Bristol City
Sheffield Wednesday v Barnsley
Wycombe Wanderers v Coventry City

Tuesday, Dec. 15, 2020
A.F.C. Bournemouth v Wycombe Wanderers
Barnsley v Preston North End
Bristol City v Millwall
Nottingham Forest v Sheffield Wednesday
Queens Park Rangers v Stoke City
Watford v Brentford

Wednesday, Dec. 16, 2020
Blackburn Rovers v Rotherham United
Cardiff City v Birmingham City
Coventry City v Huddersfield Town
Derby County v Swansea City
Middlesbrough v Luton Town
Reading v Norwich City

Saturday, Dec. 19, 2020
Birmingham City v Middlesbrough
Brentford v Reading
Huddersfield Town v Watford
Luton Town v A.F.C. Bournemouth
Millwall v Nottingham Forest
Norwich City v Cardiff City
Preston North End v Bristol City
Rotherham United v Derby County
Sheffield Wednesday v Coventry City
Stoke City v Blackburn Rovers
Swansea City v Barnsley
Wycombe Wanderers v Queens Park Rangers

Saturday, Dec. 26, 2020
A.F.C. Bournemouth v Millwall
Barnsley v Huddersfield Town
Blackburn Rovers v Sheffield Wednesday
Bristol City v Wycombe Wanderers
Cardiff City v Brentford
Coventry City v Stoke City
Derby County v Preston North End
Middlesbrough v Rotherham United
Nottingham Forest v Birmingham City
Queens Park Rangers v Swansea City
Reading v Luton Town
Watford v Norwich City

Tuesday, Dec. 29, 2020
Birmingham City v Derby County
Brentford v A.F.C. Bournemouth
Huddersfield Town v Blackburn Rovers
Luton Town v Bristol City
Millwall v Watford
Norwich City v Queens Park Rangers
Preston North End v Coventry City
Rotherham United v Barnsley
Sheffield Wednesday v Middlesbrough
Stoke City v Nottingham Forest
Swansea City v Reading
Wycombe Wanderers v Cardiff City

Saturday, Jan. 2, 2021
Birmingham City v Blackburn Rovers
Brentford v Bristol City
Huddersfield Town v Reading
Luton Town v Queens Park Rangers
Millwall v Coventry City
Norwich City v Barnsley
Preston North End v Nottingham Forest
Rotherham United v Cardiff City
Sheffield Wednesday v Derby County
Stoke City v A.F.C. Bournemouth
Swansea City v Watford
Wycombe Wanderers v Middlesbrough

Saturday, Jan. 16, 2021
A.F.C. Bournemouth v Luton Town
Barnsley v Swansea City
Blackburn Rovers v Stoke City
Bristol City v Preston North End
Cardiff City v Norwich City
Coventry City v Sheffield Wednesday
Derby County v Rotherham United
Middlesbrough v Birmingham City
Nottingham Forest v Millwall
Queens Park Rangers v Wycombe Wanderers
Reading v Brentford
Watford v Huddersfield Town

Tuesday, Jan. 19, 2021
Blackburn Rovers v Swansea City
Derby County v A.F.C. Bournemouth
Reading v Coventry City
Rotherham United v Stoke City
Sheffield Wednesday v Wycombe Wanderers
Watford v Barnsley

Wednesday, Jan. 20, 2021
Birmingham City v Preston North End
Brentford v Luton Town
Cardiff City v Queens Park Rangers
Huddersfield Town v Millwall
Norwich City v Bristol City
Nottingham Forest v Middlesbrough

Saturday, Jan. 23, 2021
A.F.C. Bournemouth v Sheffield Wednesday
Barnsley v Cardiff City
Bristol City v Huddersfield Town
Coventry City v Nottingham Forest
Luton Town v Rotherham United
Middlesbrough v Blackburn Rovers
Millwall v Norwich City
Preston North End v Reading
Queens Park Rangers v Derby County
Stoke City v Watford
Swansea City v Brentford
Wycombe Wanderers v Birmingham City

Saturday, Jan. 30, 2021
Birmingham City v Coventry City
Blackburn Rovers v Luton Town
Brentford v Wycombe Wanderers
Cardiff City v Millwall
Derby County v Bristol City
Huddersfield Town v Stoke City
Norwich City v Middlesbrough
Nottingham Forest v Barnsley
Reading v A.F.C. Bournemouth
Rotherham United v Swansea City
Sheffield Wednesday v Preston North End
Watford v Queens Park Rangers

Saturday, Feb. 6, 2021
A.F.C. Bournemouth v Birmingham City
Barnsley v Derby County
Bristol City v Cardiff City
Coventry City v Watford
Luton Town v Huddersfield Town
Middlesbrough v Brentford
Millwall v Sheffield Wednesday
Preston North End v Rotherham United
Queens Park Rangers v Blackburn Rovers
Stoke City v Reading
Swansea City v Norwich City
Wycombe Wanderers v Nottingham Forest

Saturday, Feb. 13, 2021
Birmingham City v Luton Town
Blackburn Rovers v Preston North End
Brentford v Barnsley
Cardiff City v Coventry City
Derby County v Middlesbrough
Huddersfield Town v Wycombe Wanderers
Norwich City v Stoke City
Nottingham Forest v A.F.C. Bournemouth
Reading v Millwall
Rotherham United v Queens Park Rangers
Sheffield Wednesday v Swansea City
Watford v Bristol City

Tuesday, Feb. 16, 2021
Bristol City v Reading
Luton Town v Cardiff City
Middlesbrough v Huddersfield Town
Preston North End v Watford
Stoke City v Sheffield Wednesday
Wycombe Wanderers v Derby County

Wednesday, Feb. 17, 2021
A.F.C. Bournemouth v Rotherham United
Barnsley v Blackburn Rovers
Coventry City v Norwich City
Millwall v Birmingham City
Queens Park Rangers v Brentford
Swansea City v Nottingham Forest

Saturday, Feb. 20, 2021
Bristol City v Barnsley
Cardiff City v Preston North End
Coventry City v Brentford
Huddersfield Town v Swansea City
Millwall v Wycombe Wanderers
Norwich City v Rotherham United
Nottingham Forest v Blackburn Rovers
Queens Park Rangers v A.F.C. Bournemouth
Reading v Middlesbrough
Sheffield Wednesday v Birmingham City
Stoke City v Luton Town
Watford v Derby County

Tuesday, Feb. 23, 2021
Birmingham City v Norwich City
Derby County v Huddersfield Town
Luton Town v Millwall
Middlesbrough v Bristol City
Rotherham United v Nottingham Forest
Wycombe Wanderers v Reading

Wednesday, Feb. 24, 2021
A.F.C. Bournemouth v Cardiff City
Barnsley v Stoke City
Blackburn Rovers v Watford
Brentford v Sheffield Wednesday
Preston North End v Queens Park Rangers
Swansea City v Coventry City

Saturday, Feb. 27, 2021
A.F.C. Bournemouth v Watford
Barnsley v Millwall
Birmingham City v Queens Park Rangers
Blackburn Rovers v Coventry City
Brentford v Stoke City
Derby County v Nottingham Forest
Luton Town v Sheffield Wednesday
Middlesbrough v Cardiff City
Preston North End v Huddersfield Town
Rotherham United v Reading
Swansea City v Bristol City
Wycombe Wanderers v Norwich City

Tuesday, March 2, 2021
Cardiff City v Derby County
Coventry City v Middlesbrough
Huddersfield Town v Birmingham City
Millwall v Preston North End
Nottingham Forest v Luton Town
Reading v Blackburn Rovers

Wednesday, March 3, 2021
Bristol City v A.F.C. Bournemouth
Norwich City v Brentford
Queens Park Rangers v Barnsley
Sheffield Wednesday v Rotherham United
Stoke City v Swansea City
Watford v Wycombe Wanderers

Saturday, March 6, 2021
Barnsley v Birmingham City
Brentford v Rotherham United
Bristol City v Queens Park Rangers
Coventry City v Derby County
Huddersfield Town v Cardiff City
Millwall v Blackburn Rovers
Norwich City v Luton Town
Preston North End v A.F.C. Bournemouth
Reading v Sheffield Wednesday
Stoke City v Wycombe Wanderers
Swansea City v Middlesbrough
Watford v Nottingham Forest

Saturday, March 13, 2021
A.F.C. Bournemouth v Barnsley
Birmingham City v Bristol City
Blackburn Rovers v Brentford
Cardiff City v Watford
Derby County v Millwall
Luton Town v Swansea City
Middlesbrough v Stoke City
Nottingham Forest v Reading
Queens Park Rangers v Huddersfield Town
Rotherham United v Coventry City
Sheffield Wednesday v Norwich City
Wycombe Wanderers v Preston North End

Tuesday, March 16, 2021
A.F.C. Bournemouth v Swansea City
Cardiff City v Stoke City
Derby County v Brentford
Luton Town v Coventry City
Middlesbrough v Preston North End
Rotherham United v Watford

Wednesday, March 17, 2021
Birmingham City v Reading
Blackburn Rovers v Bristol City
Nottingham Forest v Norwich City
Queens Park Rangers v Millwall
Sheffield Wednesday v Huddersfield Town
Wycombe Wanderers v Barnsley

Saturday, March 20, 2021
Barnsley v Sheffield Wednesday
Brentford v Nottingham Forest
Bristol City v Rotherham United
Coventry City v Wycombe Wanderers
Huddersfield Town v A.F.C. Bournemouth
Millwall v Middlesbrough
Norwich City v Blackburn Rovers
Preston North End v Luton Town
Reading v Queens Park Rangers
Stoke City v Derby County
Swansea City v Cardiff City
Watford v Birmingham City

Friday, April 2, 2021
A.F.C. Bournemouth v Middlesbrough
Barnsley v Reading
Birmingham City v Swansea City
Bristol City v Stoke City
Cardiff City v Nottingham Forest
Derby County v Luton Town
Huddersfield Town v Brentford
Millwall v Rotherham United
Preston North End v Norwich City
Queens Park Rangers v Coventry City
Watford v Sheffield Wednesday
Wycombe Wanderers v Blackburn Rovers

Monday, April 5, 2021
Blackburn Rovers v A.F.C. Bournemouth
Brentford v Birmingham City
Coventry City v Bristol City
Luton Town v Barnsley
Middlesbrough v Watford
Norwich City v Huddersfield Town
Nottingham Forest v Queens Park Rangers
Reading v Derby County
Rotherham United v Wycombe Wanderers
Sheffield Wednesday v Cardiff City
Stoke City v Millwall
Swansea City v Preston North End

Saturday, April 10, 2021
A.F.C. Bournemouth v Coventry City
Barnsley v Middlesbrough
Birmingham City v Stoke City
Bristol City v Nottingham Forest
Cardiff City v Blackburn Rovers
Derby County v Norwich City
Huddersfield Town v Rotherham United
Millwall v Swansea City
Preston North End v Brentford
Queens Park Rangers v Sheffield Wednesday
Watford v Reading
Wycombe Wanderers v Luton Town

Saturday, April 17, 2021
Blackburn Rovers v Derby County
Brentford v Millwall
Coventry City v Barnsley
Luton Town v Watford
Middlesbrough v Queens Park Rangers
Norwich City v A.F.C. Bournemouth
Nottingham Forest v Huddersfield Town
Reading v Cardiff City
Rotherham United v Birmingham City
Sheffield Wednesday v Bristol City
Stoke City v Preston North End
Swansea City v Wycombe Wanderers

Tuesday, April 20, 2021
Birmingham City v Nottingham Forest
Brentford v Cardiff City
Norwich City v Watford
Preston North End v Derby County
Sheffield Wednesday v Blackburn Rovers
Swansea City v Queens Park Rangers

Wednesday, April 21, 2021
Huddersfield Town v Barnsley
Luton Town v Reading
Millwall v A.F.C. Bournemouth
Rotherham United v Middlesbrough
Stoke City v Coventry City
Wycombe Wanderers v Bristol City

Saturday, April 24, 2021
A.F.C. Bournemouth v Brentford
Barnsley v Rotherham United
Blackburn Rovers v Huddersfield Town
Bristol City v Luton Town
Cardiff City v Wycombe Wanderers
Coventry City v Preston North End
Derby County v Birmingham City
Middlesbrough v Sheffield Wednesday
Nottingham Forest v Stoke City
Queens Park Rangers v Norwich City
Reading v Swansea City
Watford v Millwall

Saturday, May 1, 2021
Birmingham City v Cardiff City
Brentford v Watford
Huddersfield Town v Coventry City
Luton Town v Middlesbrough
Millwall v Bristol City
Norwich City v Reading
Preston North End v Barnsley
Rotherham United v Blackburn Rovers
Sheffield Wednesday v Nottingham Forest
Stoke City v Queens Park Rangers
Swansea City v Derby County
Wycombe Wanderers v A.F.C. Bournemouth

Saturday, May 8, 2021
A.F.C. Bournemouth v Stoke City
Barnsley v Norwich City
Blackburn Rovers v Birmingham City
Bristol City v Brentford
Cardiff City v Rotherham United
Coventry City v Millwall
Derby County v Sheffield Wednesday
Middlesbrough v Wycombe Wanderers
Nottingham Forest v Preston North End
Queens Park Rangers v Luton Town
Reading v Huddersfield Town
Watford v Swansea City
"""



import re

correct_team_names = {
    'Arsenal':'Arsenal',
    'Aston Villa':'Aston Villa',
    'Brighton':'Brighton & Hove Albion',
    'Burnley':'Burnley',
    'Chelsea':'Chelsea',
    'Crystal Palace':'Crystal Palace',
    'Everton':'Everton',
    'Fulham':'Fulham', 
    'Leeds':'Leeds United',
    'Leed':'Leeds United',
    'Leicester':'Leicester City', 
    'Liverpool':'Liverpool', 
    'Man Utd':'Manchester United',
    'Man City':'Manchester City',
    'Newcastle':'Newcastle United', 
    'Sheffield Utd':'Sheffield United',
    'Sheff Utd':'Sheffield United',
    'Sheffield United':'Sheffield United',
    'Southampton':'Southampton',
    'Spurs':'Tottenham Hotspur',
    'West Brom':'West Bromwich Albion', 
    'West Ham':'West Ham United',
    'Wolves':'Wolverhampton Wanderers',
    'A.F.C. Bournemouth':'AFC Bournemouth',
    'Barnsley':'Barnsley',
    'Birmingham City':'Birmingham City',
    'Blackburn Rovers':'Blackburn Rovers',
    'Brentford':'Brentford',
    'Bristol City':'Bristol City',
    'Cardiff City':'Cardiff City',
    'Coventry City':'Coventry City',
    'Derby County':'Derby County',
    'Huddersfield Town':'Huddersfield Town',
    'Luton Town':'Luton Town',
    'Middlesbrough':'Middlesbrough',
    'Millwall':'Millwall',
    'Norwich City':'Norwich City',
    'Nottingham Forest':'Nottingham Forest',
    'Preston North End':'Preston North End',
    'Queens Park Rangers':'Queens Park Rangers',
    'Reading':'Reading',
    'Rotherham United':'Rotherham United',
    'Sheffield Wednesday':'Sheffield Wednesday',
    'Stoke City':'Stoke City',
    'Swansea City':'Swansea City',
    'Watford':'Watford',
    'Wycombe Wanderers':'Wycombe Wanderers',
}

special_cases = {
    'May 13' :[['Aston Villa', 'Everton']],
    'January 23':[['Aston Villa', 'Newcastle United']],
    'February 17':[['Burnley', 'Fulham']],
    'December 28':[['Everton', 'Manchester City']],
    'March 21':[['Aston Villa', 'Tottenham Hotspur']],
    'May 2':[['Manchester United', 'Liverpool']]
}

months_shortened_dict = {
    'Feb.':'February',
    'Jan.':'January',
    'Dec.':'December',
    'Nov.':'November',
    'Oct.':'October',
    'Sept.':'September',
}

def get_schedule_prem() :
    schedule_dict = {}
    for line in schedule_prem.split('\n\n') :
        lines = [lin for lin in line.split('\n') if lin != '']
        date_array = [split_piece for split_piece in lines[0].split(' ') if split_piece != '']
        date = ' '.join([date_array[-1], date_array[-2]])
        if date in special_cases :
            dont_add = special_cases[date]
        else :
            dont_add = []
        games = []
        for lin in lines[1:] :
            lin = lin.split('(')[0]
            lin = ' '.join(lin.split(' ')[1:])[:-1]
            game = lin.split(' v ')
            if game != [''] :
                game = [correct_team_names[game[0]], correct_team_names[game[1]]]
                if not game in dont_add :
                    games.append(game)
        schedule_dict[date] = games
    schedule_dict['February 22'].append(['Brighton & Hove Albion', 'Crystal Palace'])
    return schedule_dict

def get_schedule_championship() :
    schedule_dict = {}
    for line in schedule_championship.split('\n\n') :
        lines = [lin for lin in line.split('\n') if lin != '']
        date = lines[0].split(',')[1][1:]
        month = date.split(' ')[0]
        if month in months_shortened_dict :
            month = months_shortened_dict[month]
            date = ' '.join([month, date.split(' ')[1]])
        games = []
        for lin in lines[1:] :
            game = lin.split(' v ')
            if game != [''] :
                game = [correct_team_names[game[0]], correct_team_names[game[1]]]
                games.append(game)
        schedule_dict[date] = games
    return schedule_dict
        
def team_in_gameday(team, gameday) :
    for game in gameday :
        if team in game :
            if team == game[0] :
                return True, game[1], get_stadium(game[0]), 0
            return True, game[0], get_stadium(game[0]), 1
    return False, '', None

def get_games_in_a_month(month, schedule, team) :
    games = {}
    for date in schedule :
        m = date.split(' ')[0]
        tig = team_in_gameday(team, schedule[date])
        if month == m and tig[0] :
            games[date] = [tig[1], tig[2], tig[3]]
    return games
    
def replace_old_teams_in_schedule(schedule, new_teams, teams_in_league) :
    old_teams = []
    for date in schedule :
        for game in schedule[date] :
            for team in game :
                if (not team in teams_in_league) and (not team in old_teams) :
                    old_teams.append(team)
    print(old_teams)
    new_schedule = {}
    for date in schedule :
        new_schedule[date] = []
        for game in schedule[date] :
            new_insertion = []
            for team in game :
                if team in old_teams :
                    new_insertion.append(new_teams[old_teams.index(team)])
                else :
                    new_insertion.append(team)
            new_schedule[date].append(new_insertion)
    return new_schedule

def scramble_schedule(schedule) :
    dates = list(schedule.keys())
    random.shuffle(dates)
    values = [schedule[date] for date in dates]
    random.shuffle(values)
    return {dates[i]:values[i] for i in range(len(values))}


"""
c = 0
schedule = get_schedule()
amount_of_games = {correct_team_names[t]:0 for t in correct_team_names}
villa_games = []
for date in schedule :
    games_on_date = schedule[date]
    for game in games_on_date :
        t1, t2 = game
        amount_of_games[t1] += 1
        amount_of_games[t2] += 1
        
        if t1 == 'Aston Villa' or t2 == 'Aston Villa' :
            if game in villa_games :
                print(game)
                print('ITS A REPEAT _________________________________________________________________________________________________________')
                print()
                print()
                print()
            else :
                villa_games.append(game)
        

for element in amount_of_games :
    print(element, amount_of_games[element])
"""

"""
schedule = get_schedule_championship()
print()
print()
print()
for date in schedule :
    print(date, schedule[date])
    print()
"""
