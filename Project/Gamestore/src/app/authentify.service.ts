import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';
import { Login } from './login';

@Injectable({
    providedIn: 'root'
  })
  export class AuthService {
    BASE_URL = 'http://localhost:8000';
  
    constructor(
      private http: HttpClient
    ) { }
  
    login(username, password): Observable<Login> {
      return this.http.post<Login>(`${this.BASE_URL}/api/login/`, {
        username,
        password
      });
    }
  }