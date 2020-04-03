import { Component, OnInit } from '@angular/core';
import { Job } from '../job';
import {JobsService} from '../jobs.service';

@Component({
  selector: 'app-jobs',
  templateUrl: './jobs.component.html',
  styleUrls: ['./jobs.component.css']
})
export class JobsComponent implements OnInit {

  public jobs:Job[];

  constructor( private jobsService:JobsService) { }

  ngOnInit(): void {

    this.getJobs();
  }

  getJobs() {
      this.jobsService.getJobs()
      .subscribe(jobs=>this.jobs=jobs)
  }

}