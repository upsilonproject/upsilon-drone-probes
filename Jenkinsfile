#!groovy                                                                           

properties(                                                                        
    [                                                                              
        [                                                                          
            $class: 'jenkins.model.BuildDiscarderProperty', strategy: [$class: 'LogRotator', numToKeepStr: '10', artifactNumToKeepStr: '10'],
            $class: 'CopyArtifactPermissionProperty', projectNames: '*'            
        ]                                                                          
    ]                                                                              
)   

def prepareEnv() {                                                                 
    unstash 'binaries'                                                             
                                                                                   
    env.WORKSPACE = pwd()                                                          
                                                                                   
    sh "find ${env.WORKSPACE}"                                                     
                                                                                   
    sh 'mkdir -p SPECS SOURCES'                                                    
    sh "cp dist/*.zip SOURCES/upsilon-serviceChecks.zip"                      
}                                                                                 

def buildRpm(dist) {                                                               
    deleteDir()                                                                    

	prepareEnv()
                                                                                                                                                                      
    sh 'unzip -jo SOURCES/upsilon-serviceChecks-*.zip "upsilon-serviceChecks-*/var/pkg/upsilon-serviceChecks.spec" "upsilon-serviceChecks-*/.buildid.rpmmacro" -d SPECS/'
    sh "find ${env.WORKSPACE}"                                                     
                                                                                   
    sh "rpmbuild -ba SPECS/upsilon-serviceChecks.spec --define '_topdir ${env.WORKSPACE}' --define 'dist ${dist}'"
                                                                                   
    archive 'RPMS/noarch/*.rpm'                                                    
}                    

node {
	stage "Build"

	deleteDir()
	checkout scm

	sh './make.sh'

	stash includes: 'dist/*.zip', name: 'binaries'
}

stage "Package"

node {                                                                             
    buildRpm("el7")                                                                
}                                                                                  
                                                                                   
node {                                                                             
    buildRpm("el6")                                                                
}                                                                                  
                                                                                   
node {                                                                             
    buildRpm("fc24")                                                               
}


