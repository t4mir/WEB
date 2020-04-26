import { Component, OnInit } from '@angular/core';
import {AuthService} from '../authentify.service';
import {Router} from '@angular/router';

@Component({
  selector: 'app-loginpage',
  templateUrl: './loginpage.component.html',
  styleUrls: ['./loginpage.component.css']
})
export class LoginpageComponent implements OnInit {
  logged = false;
  username = '';
  password = '';

  constructor(
    private router: Router,
    private authentify: AuthService
  ) { }

  ngOnInit(): void {
    const token = localStorage.getItem('token');
    if (token){
      this.logged = true;
    }
  }

  login() {
    this.authentify.login(this.username, this.password)
      .subscribe(res => {
        localStorage.setItem('token', res.token);
        this.logged = true;
        this.username = '';
        this.password = '';
      });
  }

  logout(): void {
    localStorage.clear();
    this.logged = false;
  }

}