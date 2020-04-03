import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { JobDetailComponent } from './job-detail/job-detail.component';
import { JobsComponent } from './jobs/jobs.component';





  const appRoutes: Routes = [
    {path:'',redirectTo:'jobs',component:AppComponent},
    {path:'jobs/:id',component:JobDetailComponent}
  ]
   
@NgModule({
  declarations: [
    AppComponent,
    JobsComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    RouterModule.forRoot(appRoutes)
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
