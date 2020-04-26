import { Injectable } from '@angular/core';
import { Games } from '../app/category';
import { Observable, of } from 'rxjs';
import { catchError, map, tap } from 'rxjs/operators';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ProductService {
  constructor(private http: HttpClient) {}
  BASE_URL = 'http://localhost:8000';

  getProductbyId (id): Observable<Games> {
    return this.http.get<Games>(`${this.BASE_URL}/api/games/${id}`)
  }

  getWholeGames ():Observable<Games[]> {
    return this.http.get<Games[]>(`${this.BASE_URL}/api/games`);
  }

}
