import { Component, OnInit } from '@angular/core';
import {  Job } from '../job';
import {ActivatedRoute} from '@angular/router';
import {JobsService} from '../jobs.service';

@Component({
  selector: 'app-job-detail',
  templateUrl: './job-detail.component.html',
  styleUrls: ['./job-detail.component.css']
})
export class JobDetailComponent implements OnInit {


  job:Job;
  public viewCount : number = 0;
  constructor(private jobsService: JobsService,
    private route: ActivatedRoute) { }
  
  ngOnInit(): void {
   
    
  }
  getCity(){
    const id = +this.route.snapshot.paramMap.get('id');
    this.jobsService.getJob(id)
    .subscribe(job => this.job = job);
  }
  
}

