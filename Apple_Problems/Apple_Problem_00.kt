/*
This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
*/
fun main(args : Array<String>) {
    val jobScheduler : JobScheduler = JobScheduler()
    jobScheduler.schedule({ println("Scheduled Function") },100)

}
class JobScheduler(){
    fun schedule(function : ()-> Unit,n : Int){
        Thread.sleep(n.toLong())
        function()
    }
}
