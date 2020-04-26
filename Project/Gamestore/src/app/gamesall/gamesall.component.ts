import { Component, OnInit } from '@angular/core';
import { GameService } from '../game.service';
import { Games } from '../category'

@Component({
  selector: 'app-gamesall',
  templateUrl: './gamesall.component.html',
  styleUrls: ['./gamesall.component.css']
})
export class GamesallComponent implements OnInit {

  games : Games[] = [];

  constructor(private gameServ : GameService) { }

  ngOnInit(): void {
    this.getAllGames();
  }

  getAllGames() {
    this.gameServ.getGames().subscribe(gam => this.games = gam);
  }

}
