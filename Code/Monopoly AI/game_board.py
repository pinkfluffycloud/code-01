#!/usr/bin/env python3

game = {
	"Go": {"type": "Go", "position": 0},
	"Old Kent Road": {"type": "property", "color": "brown", "price": 60, "rent": [2, 10, 30, 90, 160, 250], "is_owned": False, "position": 1},
	"Community Chest": {"type": "community_chest", "position": 2},
	"Whitechapel Road": {"type": "property", "color": "brown", "price": 60, "rent": [4, 20, 60, 180, 320, 450], "is_owned": False, "position": 3},
	"Income Tax": {"type": "tax", "position": 4, "amount": 200},
	"Kings Cross Station": {"type": "property", "color": "railroad", "price": 200, "rent": [25, 50, 100, 200], "is_owned": False, "position": 5},
	"The Angel Islington": {"type": "property", "color": "light_blue", "price": 100, "rent": [6, 30, 90, 270, 400, 550], "is_owned": False, "position": 6},
	"Chance": {"type": "chance", "position": 7},
	"Euston Road": {"type": "property", "color": "light_blue", "price": 100, "rent": [6, 30, 90, 270, 400, 550], "is_owned": False, "position": 8},
	"Pentonville Road": {"type": "property", "color": "light_blue", "price": 120, "rent": [8, 40, 100, 300, 450, 600], "is_owned": False, "position": 9},
	"Just Visiting": {"type": "just visiting", "position": 10},
	"Jail": {"type": "jail", "position": 10},
	"Pall Mall": {"type": "property", "color": "purple", "price": 140, "rent": [10, 50, 150, 450, 625, 750], "is_owned": False, "position": 11},
	"Electric Company": {"type": "property", "color": "utility", "price": 150, "rent": [4, 10], "is_owned": False, "position": 12},
	"Whitehall": {"type": "property", "color": "purple", "price": 140, "rent": [10, 50, 150, 450, 625, 750], "is_owned": False, "position": 13},
	"Northumberland Avenue": {"type": "property", "color": "purple", "price": 160, "rent": [12, 60, 180, 500, 700, 900], "is_owned": False, "position": 14},
	"Marylebone Station": {"type": "property", "color": "railroad", "price": 200, "rent": [25, 50, 100, 200], "is_owned": False, "position": 15},
	"Bow Street": {"type": "property", "color": "orange", "price": 180, "rent": [14, 70, 200, 550, 750, 950], "is_owned": False, "position": 16},
	"Community Chest": {"type": "community_chest", "position": 17},
	"Marlborough Street": {"type": "property", "color": "orange", "price": 180, "rent": [14, 70, 200, 550, 750, 950], "is_owned": False, "position": 18},
	"Vine Street": {"type": "property", "color": "orange", "price": 200, "rent": [16, 80, 220, 600, 800, 1000], "is_owned": False, "position": 19},
	"Free Parking": {"type": "free_parking", "position": 20},
	"Strand": {"type": "property", "color": "red", "price": 220, "rent": [18, 90, 250, 700, 875, 1050], "is_owned": False, "position": 21},
	"Chance": {"type": "chance", "position": 22},
	"Fleet Street": {"type": "property", "color": "red", "price": 220, "rent": [18, 90, 250, 700, 875, 1050], "is_owned": False, "position": 23},
	"Trafalgar Square": {"type": "property", "color": "red", "price": 240, "rent": [20, 100, 300, 750, 925, 1100], "is_owned": False, "position": 24},
	"Fenchurch St. Station": {"type": "property", "color": "railroad", "price": 200, "rent": [25, 50, 100, 200], "is_owned": False, "position": 25},
	"Leicester Square": {"type": "property", "color": "yellow", "price": 260, "rent": [22, 110, 330, 800, 975, 1150], "is_owned": False, "position": 26},
	"Coventry Street": {"type": "property", "color": "yellow", "price": 260, "rent": [22, 110, 330, 800, 975, 1150], "is_owned": False, "position": 27},
	"Water Works": {"type": "property", "color": "utility", "price": 150, "rent": [4, 10], "is_owned": False, "position": 28},
	"Piccadilly": {"type": "property", "color": "yellow", "price": 280, "rent": [24, 120, 360, 850, 1025, 1200], "is_owned": False, "position": 29},
	"Go To Jail": {"type": "go_to_jail", "position": 30},
	"Regent Street": {"type": "property", "color": "green", "price": 300, "rent": [26, 130, 390, 900, 1100, 1275], "is_owned": False, "position": 31},
	"Oxford Street": {"type": "property", "color": "green", "price": 300, "rent": [26, 130, 390, 900, 1100, 1275], "is_owned": False, "position": 32},
	"Community Chest": {"type": "community_chest", "position": 33},
	"Bond Street": {"type": "property", "color": "green", "price": 320, "rent": [28, 150, 450, 1000, 1200, 1400], "is_owned": False, "position": 34},
	"Liverpool St. Station": {"type": "property", "color": "railroad", "price": 200, "rent": [25, 50, 100, 200], "is_owned": False, "position": 35},
	"Chance": {"type": "chance", "position": 36},
	"Park Lane": {"type": "property", "color": "blue", "price": 350, "rent": [35, 175, 500, 1100, 1300, 1500], "is_owned": False, "position": 37},
	"Super Tax": {"type": "tax", "position": 38, "amount": 75},
	"Mayfair": {"type": "property", "color": "blue", "price": 400, "rent": [50, 200, 600, 1400, 1700, 2000], "is_owned": False, "position": 39}
}