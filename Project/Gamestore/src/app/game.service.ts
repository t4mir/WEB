import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Games } from './category';

@Injectable({
  providedIn: 'root'
})
export class GameService {

  constructor(private http : HttpClient) { }

  getGames() : Observable <Games[]> {
    return this.http.get<Games[]>('http://localhost:8000/api/games')
  }
  getDetailGame(id): Observable<Games> {
    return this.http.get<Games>(`http://localhost:8000/api/games/${id}`)
  }
}
