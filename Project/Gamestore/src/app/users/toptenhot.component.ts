import { Component, OnInit } from '@angular/core';
import { UserService } from '../user.service';
import { User } from '../user';

@Component({
  selector: 'app-toptenhot',
  templateUrl: './toptenhot.component.html',
  styleUrls: ['./toptenhot.component.css']
})
export class ToptenhotComponent implements OnInit {

  constructor(private userServ : UserService) { }
  users : User[] = []
  ngOnInit(): void {
    this.getUsers();
  }

  getUsers () {
    this.userServ.getUsers().subscribe(user => this.users = user);
  }

}
