import { InMemoryDbService } from 'angular-in-memory-web-api';
import { Games } from './category';
import { Injectable } from '@angular/core';
import { Strategy, Sport, Simulator, Actions } from './categories';

@Injectable({
  providedIn: 'root',
})
export class InMemoryDataService implements InMemoryDbService {
  createDb() {
    const games = [
      { id: 4, name: 'Strategy', products: Strategy },
      { id: 2, name: 'Sport', products: Sport},
      { id: 3, name: 'Simulator', products: Simulator },
      { id: 1, name: 'Action', products: Actions }
    ];
    return {games};
  }
  // genId(games: Games[]): number {
  //   return games.length > 0 ? Math.max(...games.map(game => game.id)) + 1 : 1;
  // }
}