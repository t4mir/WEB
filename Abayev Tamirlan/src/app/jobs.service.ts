import { Injectable } from '@angular/core';
import { Job } from './job';
import { JOBS } from './jobs';
import { Observable, of} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class JobsService {

  constructor() { }
  getJobs():Observable<Job[]>{

    return of(JOBS);
  }

  getJob(id:number):Observable<Job> {
    return of(JOBS.find(job=>job.id===id));
  }
}

